from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class Post(models.Model):
    title = models.CharField(_('제목'), max_length=150)
    slug = models.SlugField(_('슬러그'), max_length=150)
    content = models.TextField(_('내용'))
    author = models.ForeignKey(
        User,
        verbose_name=_("작성자"),
        on_delete=models.SET_NULL,
        null=True,
        related_name='posts',
        related_query_name='post'
    )
    author_name = models.CharField(_("유저이름"), max_length=150)
    likes = models.ManyToManyField(
        User,
        verbose_name=_("좋아요"),
        related_name='likes',
        related_query_name='like',
        through='blog.Like'
    )
    tags = models.ManyToManyField(
        'blog.Tag',
        verbose_name=_("태그"),
        related_name='tags',
        related_query_name='tag'
    )
    created_at = models.DateTimeField(_("생성일"), auto_now_add=True)
    updated_at = models.DateTimeField(_("수정일"), auto_now=True)

    class Meta:
        db_table = 'POST'


class Tag(models.Model):
    name = models.CharField(_("태그명"), max_length=8)

    class Meta:
        db_table = 'TAG'


class Like(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name=_("좋아요 유저"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,
        related_name='user_likes',
        related_query_name='user_like'
    )
    username = models.CharField(_("유저이름"), max_length=150)
    post = models.ForeignKey(
        Post,
        verbose_name=_("좋아요 글"),
        on_delete=models.CASCADE,
        related_name='post_likes',
        related_query_name='post_like'
    )
    reg_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'LIKE'
        constraints = [
            models.UniqueConstraint(fields=['post', 'user'], name='only_one_like')
        ]
