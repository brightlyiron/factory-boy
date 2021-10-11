import factory

from blog.models import Like


class LikeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Like
        django_get_or_create = ('id',)

    id = factory.Sequence(lambda n: n + 1)
    user = factory.SubFactory('account.tests.factories.user.UserFactory')
    post = factory.SubFactory('blog.tests.factories.post.PostFactory')
    username = factory.PostGeneration(lambda obj, created, extracted, **kwargs: obj.user.username)

