# Generated by Django 3.2.7 on 2021-10-03 14:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=8, verbose_name='태그명')),
            ],
            options={
                'db_table': 'TAG',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='제목')),
                ('slug', models.SlugField(max_length=150, verbose_name='슬러그')),
                ('content', models.TextField(verbose_name='내용')),
                ('author_name', models.CharField(max_length=150, verbose_name='유저이름')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성일')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정일')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', related_query_name='post', to=settings.AUTH_USER_MODEL, verbose_name='작성자')),
                ('tag', models.ManyToManyField(related_name='tags', related_query_name='tag', to='blog.Tag', verbose_name='태그')),
            ],
            options={
                'db_table': 'POST',
            },
        ),
    ]