import factory
from django.contrib.auth.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ('id',)

    id = factory.sequence(lambda n: n + 1)
    username = factory.sequence(lambda n: f"user{n}" if n > 9999 else "user" + f"{n}".zfill(5))
    password = factory.PostGeneration(lambda user, create, extracted: user.set_password(user.username))
