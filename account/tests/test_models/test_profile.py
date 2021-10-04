import logging

import pytest

from account.tests.factories.profile import ProfileFactory
from account.tests.factories.user import UserFactory

profile_model = ProfileFactory._meta.model

pytestmark = pytest.mark.django_db

logger = logging.getLogger('test_profile_model')

test_username = 'profile2021'


@pytest.mark.django_db(transaction=True)
@pytest.fixture(scope='module', autouse=True)
def test_user_factory(django_db_setup, django_db_blocker):
    global test_username
    with django_db_blocker.unblock():
        user = UserFactory(id=2, username=test_username)
        assert isinstance(user.profile, profile_model)


def test_nickname_fields():
    global test_username
    user = UserFactory(id=2)
    assert user.profile.nickname == user.username


def test_nickname_field_max_length():
    max_length = 30
    username_max_length = profile_model._meta.get_field('nickname').max_length
    assert max_length == username_max_length


def test_phone_number_field_max_length():
    max_length = 11
    phone_max_length = profile_model._meta.get_field("phone_number").max_length
    assert max_length == phone_max_length


def test_str_method():
    global test_username
    user = UserFactory(id=2)
    assert test_username == str(user.profile)


def test_get_short_nickname():
    global test_username
    user = UserFactory(id=2)
    assert test_username[:5] == user.profile.get_short_nickname()
