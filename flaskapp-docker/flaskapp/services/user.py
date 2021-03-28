"""The definition of UserService."""
from typing import Optional

from flaskapp.models.models import User
from flaskapp.repos.user import UserRepository


class UserService:
    """The definition of the service."""
    def __init__(self, users: UserRepository):
        """The initiation function.
        Args:
            users: A user repository object.
        """
        self._users = users

    def add_by_name_email(self, name: str, email: str) -> Optional[User]:
        """Adds a user to the database."""
        self._users.add(User(username=name, email=email))
        self._users.commit()
