import pytest

from blog.models import Post
from blog.tests.factories.post import PostFactory, PostWithLikeFactory

pytestmark = pytest.mark.django_db


def test_post_factory():
    assert isinstance(PostFactory(), Post)


def test_post_with_like_factory():
    assert isinstance(PostWithLikeFactory(), Post)


def test_post_factory_like_count():
    post = PostFactory()
    like_count = post.likes.count()
    assert 0 == like_count


def test_post_with_like_factory_like_count():
    post = PostWithLikeFactory()
    like_count = post.likes.count()
    assert 1 == like_count
