"""The tests related to the User model."""
import pytest
from flaskapp.models.models import User
from flaskapp.services import get_user_service
from flaskapp.services.user import UserService

from flaskapp.tests.repos.helpers import create_in_memory_database


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
def service():
    """Fixture for the tests."""
    db = create_in_memory_database(data=TEST_DATA)
    return get_user_service(db=db)


def test_service_can_be_instantiated(service):
    """Tests the creation of the service."""
    assert isinstance(service, UserService)


def test_add_by_name_email_adds_new_user(service):
    """Tests we can add a user by name and email."""
    new_user_name = 'Josh'
    new_user_email = 'j@j.com'
    users = service._users.all()

    assert len(users) == len(TEST_DATA[User])

    service.add_by_name_email(name=new_user_name, email=new_user_email)

    users = service._users.all()

    assert len(users) == len(TEST_DATA[User]) + 1

    assert users[len(TEST_DATA)].username == new_user_name
    assert users[len(TEST_DATA)].email == new_user_email
