import factory

from blog.models import Post


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post
        django_get_or_create = ('id',)

    id = factory.Sequence(lambda n: n + 1)
    title = factory.Faker('sentence')
    slug = factory.LazyAttribute(lambda post: post.title)
    content = factory.Faker('words')
    author = factory.SubFactory('account.tests.factories.user.UserFactory')
    author_name = factory.PostGeneration(lambda obj, create, extracted, **kwargs: obj.author.username)

    @factory.post_generation
    def tags(self, create, extracted, **kwargs):
        # Simple ManyToMany 경우 별도 필드를 지원하지 않고 생성 시 리스트로 추가 할 수 있도록 만든다.
        if not create:
            return

        if extracted:
            for tag in extracted:
                self.tags.add(tag)

    @factory.post_generation
    def likes(self, create, extracted, **kwargs):
        # Thorough 로 설정된 M:N 관계인 경우에도 likes 필드로 관계를 형성시킬 수 있다.
        if not create:
            # PostFactory(), .build() 무시
            return
        if extracted:
            # 인자값이 들어온다면
            for like in extracted:
                self.likes.add(like)


class PostWithLikeFactory(PostFactory):
    # Through 설정된 M:N의 경우 별도의 팩토리를 만들어 생성시 관계를 형성할 수 있도록 할 수 있다.
    like = factory.RelatedFactory(
        'blog.tests.factories.like.LikeFactory',
        # LikeFactory 의 SubFactory 가 동작하지 않도록 반드시 factory_related_name 지정해줘야 한다.
        factory_related_name='post'
    )
