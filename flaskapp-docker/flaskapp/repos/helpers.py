"""The definition of helpers for the repositories."""
from math import ceil

class Pagination:
    """A simple Pagination object.

    Used to help with some of the calculations of the various data that might
    be useful for pagination."""

    def __init__(self, total_results, current_page, items_per_page):
        """Instantiate a Pagination object with the required data.

        Args:
            total_results (int):    Total result count without filters.
            current_page (int):     Current page number we are on.
            items_per_page (int):   Amount of items to be displayed per page.
        """
        self.total_results = total_results
        self.current_page = current_page
        self.items_per_page = items_per_page
        self.total_pages = int(ceil(total_results / items_per_page))
        self.current_page_start = ((current_page - 1) * items_per_page) or 1
        self.current_page_end = min(current_page * items_per_page, total_results)

    def to_dict(self):
        """Helper to return the class params as a dict."""
        return {
            'total_results': self.total_results,
            'current_page': self.current_page,
            'items_per_page': self.items_per_page,
            'total_pages': self.total_pages,
            'current_page_start': self.current_page_start,
            'current_page_end': self.current_page_end,
        }


class EntityList(list):
    """A simple class to extend the standard python list for entities.

    This allows for any metadata, pagination details etc. to be placed onto
    the list rather than just returning a simple python list of entities.

    The custom class behaves as you would expect the normal list returned by
    our queries to behave so it should be invisible to the user but it has
    specific parameters that can be got at such as `entity_list.pagination`
    to get pagination data.
    """

    def __init__(self, items, pagination=None):
        """Initialise an EntityList.

        Args:
            items (list):       Standard python list of entities.
            pagination (obj):   Specific Pagination object.
        """
        super(EntityList, self).__init__(items)

        self.pagination = pagination
