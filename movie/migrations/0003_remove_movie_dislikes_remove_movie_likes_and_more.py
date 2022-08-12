# Generated by Django 4.1 on 2022-08-10 22:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movie', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='dislikes',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='likes',
        ),
        migrations.AlterField(
            model_name='movie',
            name='movie_length',
            field=models.CharField(max_length=100),
        ),
        migrations.AddField(
            model_name='movie',
            name='dislikes',
            field=models.ManyToManyField(related_name='movie_dislikes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='movie',
            name='likes',
            field=models.ManyToManyField(related_name='movie_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
