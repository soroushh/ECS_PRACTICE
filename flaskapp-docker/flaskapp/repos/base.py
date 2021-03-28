"""Base repository definition to be extended by specific repositories."""
from sqlalchemy.orm import joinedload
from sqlalchemy.sql import asc, desc

from .helpers import EntityList, Pagination


class BaseRepository:
    """Base repository used to abstract away related queries.

    The only requirement is that this class is extended by your own class and
    the _model private class attribute overwritten. There should be one
    repository per entity and any specific queries should be written in the
    child repository.

    The `_list` class attribute can also be overwritten to provide custom
    collection methods for working with the data. Please see PalletList for
    an example of this in use.

    At the moment this has some dependencies on SqlAlchemy that in the long
    run I would like to move away from so we can switch out the db for a
    Redis instance for example seamlessly but for now this should be seen
    as an abstraction tool used to make testing and construction of queries
    easier.

    Example Construction:
        class UserRepository(BaseRepository):

            _model = User

            def find_users_by_first_name(self, first_name):
                return self._build_list(
                    self._query(filters=[User.first_name == first_name])
                )

    Example Usage:
        >>> user_repo = UserRepository(db=db)
        >>> user_repo.find_users_by_first_name(first_name='Peter')
        EntityList(User('Peter Featherstone'), User('Peter Jones'))
    """

    _model = None
    _list = EntityList

    def __init__(self, db) -> None:
        """Instantiate the repository with a db session."""
        self._db = db

    def get(self, _id, **kwargs):
        """Return a _model by it's primary key id.

        We fake the standard way of searching by primary key which allows
        us to go through our _query method to get the sanitisation and
        pre-processing that we need.

        Returns:
            obj: An individual _model instance.
        """
        return self._query(
            filters=[
                self._model.__mapper__.primary_key[0] == _id
            ],
            **kwargs
        ).first()

    def get_by_ids(self, ids: list) -> EntityList:
        """Return a list of models by their ids.

        Args:
            ids (list): model ids.

        Returns:
            obj: An EntityList.
        """
        return self._build_list(
            self._query(filters=[
                self._model.__mapper__.primary_key[0].in_(ids)
            ])
        )

    def all(self, **kwargs) -> EntityList:
        """Return all _models.

        Returns:
            An EntityList containing returned models of type self._model.
        """
        return self._build_list(self._query(**kwargs))

    def filter(
        self, joins_: set = None, filters_: set = None, **kwargs
    ) -> EntityList:
        """Generic filter function for searching entities.

        This shouldn't be used for anything other than allowing generic
        searching across any of the internal fields in a client search, mainly
        this should be for graphQL queries or search functionality.

        Currently this will only allow simple key=value type searching rather
        than likes, greater than searches etc. For more complex behaviour
        individual repositories will need to overwrite this method for their
        own purposes and pass in specific joins_ or filters_ to this method.

        Always prefer explicit named functions for queries over this.

        Args:
            joins_: A set of joins needed to perform the filter.
            filters_: A set of specific filters to be performed.
            **kwargs: key: value pairs of attributes to search on.

        Returns:
            An EntityList containing returned models of type self._model.
        """
        filters = filters_ or set()
        for attr, value in kwargs.items():
            filters.add(getattr(self._model, attr) == value)

        return self._build_list(self._query(joins=joins_, filters=filters))

    def add(self, entity) -> None:
        """Add an entity to the current session.

        Args:
            entity (obj): An entity to add.
        """
        self._db.add(entity)

    def delete(self, entity, hard: bool = False) -> None:
        """Delete an entity.

        If the model has the deleted attribute we soft delete by default. This
        can be overriden using the `hard` param.

        Args:
            entity (obj): An entity to delete.
            hard (bool): Specify a hard delete. Defaults to False.
        """
        if hasattr(self._model, 'deleted') and not hard:
            entity.deleted = True

        else:
            self._db.delete(entity)

    def commit(self) -> None:
        """Commit all changes to persistence."""
        self._db.commit()

    def _query(self, **kwargs):
        """Wrap the query so we can pre-process it.

        Going through here as the final sanitisation check is important as it
        does things like filtering out deleted items automatically. There are
        a number of kwargs to help customise the returned items.

        Args:
            model (str):            Overwrite the default queried model.
            joins (list):           Joins that need to be performed.
            outer_joins (list):     Left outer joins that need to be performed.
            eager_joins(list):      Eager joins that need to be performed.
            filters (list):         Filters for the query.
            include_deleted (bool): Indicate including deleted items.
                                    Defaults to false.
            order_type (str):       Define the order type for the returned
                                    items.
                                    Defaults to asc
            order_by (str):         Set an order field for the returned items.
            group_by (str):         Set a qroup by to the query.
            size (int):             Limits the amount of items returned.
                                    Defaults to 50 when page is used.
            page (int):             Page to start returning items from.
                                    Useful for pagination
            paginate (bool):        Indicate if you want pagination info
                                    returned as part of the EntityList.
                                    Defaults to false.
            count (bool):           Indicate if you just want a row count.
                                    Defaults to false.

        Returns:
            obj: A Query object.
        """
        model = kwargs.get('model', self._model)

        query = self._db.query(model)

        if kwargs.get('joins'):
            for join in kwargs.get('joins'):
                query = query.join(join)

        if kwargs.get('outer_joins'):
            for join in kwargs.get('outer_joins'):
                query = query.outerjoin(join)

        if kwargs.get('eager_joins'):
            for join in kwargs.get('eager_joins'):
                query = query.options(joinedload(*join))

        if kwargs.get('filters'):
            for query_filter in kwargs.get('filters'):
                query = query.filter(query_filter)

        if hasattr(model, 'deleted') and not kwargs.get('include_deleted'):
            query = query.filter(model.deleted.isnot(True))

        if kwargs.get('order_by'):
            order_type_func = (
                asc if kwargs.get('order_type', 'asc') == 'asc' else desc
            )
            query = query.order_by(order_type_func(kwargs.get('order_by')))

        if kwargs.get('size'):
            query = query.limit(kwargs.get('size'))

        if kwargs.get('page'):
            query = query.offset(
                (kwargs.get('page') - 1) * kwargs.get('size', 50)
            )

        # This feels dirty, abusing pythons ability to define new private
        # attributes on an obj on the fly but I can't find a cleaner way.
        query._paginate = True if kwargs.get('paginate') else False

        if kwargs.get('group_by'):
            query = query.group_by(kwargs.get('group_by'))

        if kwargs.get('count'):
            return query.count()

        return query

    def _build_list(self, query) -> EntityList:
        """Build an EntityList based on the query.

        This is used to build a custom List class around the simple python
        list that is usually returned by query.

        It allows us to place any metadata into the list that we can get at
        in any calling layers without putting the strain on the consumer
        of our repositories.

        For example, if the `paginate=True` kwarg is passed to any repository
        method that builds a list internally then a Pagination object will be
        created and added to the list.

        The list can be changed in the child repository by overwriting the
        class level variable `_list`.

        Args:
            query (obj): A Query object.

        Returns:
            An EntityList containing returned models of type self._model.
        """
        return self._list(
            items=query.all(),
            pagination=Pagination(
                total_results=int(
                    query.limit(None).offset(None).order_by(None).count()
                ),
                # This feels dirty, abusing pythons ability to look at private
                # attributes of an obj but I can't find a cleaner way.
                current_page=int((query._offset / query._limit) + 1),
                items_per_page=int(query._limit)
            ) if query._paginate else None
        )
