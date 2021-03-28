"""The module covers services for doing creation, update and delete actions."""
from flaskapp.db.database import db as default_database
from flaskapp.repos import get_user_repository

from .user import UserService


def get_user_service(db=None):
    """The factory to create a user service."""
    db = db or default_database.session

    return UserService(users=get_user_repository(db=db))
