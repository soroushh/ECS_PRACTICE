"""The definition of the repository for querying user models."""
from .base import BaseRepository

from flaskapp.models.models import User

    class UserRepository(BaseRepository):
    _model = User

    def by_name(self, name):
        """."""
        return self._query(filters=[self._model.username == name]).first()
