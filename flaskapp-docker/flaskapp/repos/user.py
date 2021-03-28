"""The definition of the repository for querying user models."""
from flaskapp.models.models import User

from .base import BaseRepository


class UserRepository(BaseRepository):
    _model = User

    def by_name(self, name):
        """."""
        return self._query(filters=[self._model.username == name]).first()
