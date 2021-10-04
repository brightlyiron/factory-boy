import logging

import factory
from django.contrib.auth.models import User

from account.tests.factories.profile import ProfileFactory


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ('id',)

    id = factory.sequence(lambda n: n + 1)
    username = factory.sequence(lambda n: f"user{n}" if n > 9999 else f"user{n:0>4}")
    password = factory.PostGeneration(lambda user, create, extracted: user.set_password(user.username))
    profile = factory.RelatedFactory(ProfileFactory, factory_related_name='user',
                                     nickname=factory.LazyAttribute(lambda builder: builder.user.username))
