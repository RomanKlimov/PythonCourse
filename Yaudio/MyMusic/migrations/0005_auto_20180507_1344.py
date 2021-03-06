# Generated by Django 2.0 on 2018-05-07 13:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MyMusic', '0004_artist_photo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Action',
        ),
        migrations.RemoveField(
            model_name='like',
            name='playlist',
        ),
        migrations.RemoveField(
            model_name='playlist',
            name='liked',
        ),
        migrations.AddField(
            model_name='audio',
            name='liked',
            field=models.ManyToManyField(related_name='liked', through='MyMusic.Like', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='like',
            name='audio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='MyMusic.Audio'),
        ),
        migrations.AlterField(
            model_name='like',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
