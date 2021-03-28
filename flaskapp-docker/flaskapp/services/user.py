"""The definition of UserService."""
from flaskapp.repos.user import UserRepository
from flaskapp.models.models import User

class UserService():
    """The definition of the service."""
    def __init__(self, users):
        """."""
        self._users = users


    def add_by_name_email(self, name, email):
        """Adds a user to the database."""
        self._users.add(User(username=name, email=email))
        self._users.commit()
