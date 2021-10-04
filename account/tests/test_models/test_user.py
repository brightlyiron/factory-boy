import logging

import pytest

from account.tests.factories.user import UserFactory

user_model = UserFactory._meta.model

pytestmark = pytest.mark.django_db

logger = logging.getLogger('test_user_model')

test_username = 'study2021'


@pytest.mark.django_db(transaction=True)
@pytest.fixture(scope='module', autouse=True)
def test_user_factory(django_db_setup, django_db_blocker):
    global test_username
    with django_db_blocker.unblock():
        assert isinstance(UserFactory(id=1, username=test_username), user_model)


def test_fields():
    global test_username
    user = UserFactory(id=1)
    assert test_username == user.username
    assert user.check_password(test_username)


def test_username_field():
    max_length = 150
    username_max_length = user_model._meta.get_field('username').max_length
    assert max_length == username_max_length


def test_password_field():
    max_length = 128
    password_max_length = user_model._meta.get_field('password').max_length
    assert max_length == password_max_length
