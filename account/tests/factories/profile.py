import factory
import datetime

from account.models import Profile


class ProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Profile
        django_get_or_create = ('user',)

    id = factory.sequence(lambda n: n + 1)
    # We pass in profile=None to prevent UserFactory from creating another profile
    # (this disables the RelatedFactory)
    user = factory.SubFactory('account.tests.factories.user.UserFactory', profile=None)
    nickname = None
    phone_number = factory.sequence(lambda n: f"0101234{n:0>4}")
    birth_date = factory.Sequence(lambda n: datetime.date(2000, 1, 1) + datetime.timedelta(days=n))
