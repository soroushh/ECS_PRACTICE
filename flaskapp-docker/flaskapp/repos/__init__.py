"""The factories to create different repositories."""
from flaskapp.db.database import db as default_database
from flaskapp.models.models import User

from .user import UserRepository


def get_user_repository(db=None) -> UserRepository:
    """The factory to create a UserRepository."""
    db = db or default_database.session

    return UserRepository(db=db)
