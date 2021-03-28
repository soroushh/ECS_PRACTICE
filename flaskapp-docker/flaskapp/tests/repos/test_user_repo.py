"""Covers the tests related to the user repository."""
import pytest
from flaskapp.models.models import User
from flaskapp.repos import get_user_repository
from flaskapp.repos.user import UserRepository

from .helpers import create_in_memory_database

TEST_DATA = {
    User: [
        {
            'username': 'Soroush',
            'email': 's@s.com'
        },
        {
            'username': 'Farnaz',
            'email': 'f@f.com'
        }
    ]
}
@pytest.fixture()
def repository():
    """Fixture for the tests."""
    return get_user_repository(db=create_in_memory_database(data=TEST_DATA))


def test_repository_can_be_instantiated(repository):
    """Tests we can create the repository."""
    assert isinstance(repository, UserRepository)


def test_find_by_name_fetches_the_expected_user(repository):
    """Tests we can find a user by its name."""
    user = repository.by_name(name='Soroush')

    assert user.username == 'Soroush'
    assert user.email == 's@s.com'

