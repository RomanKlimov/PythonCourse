# Generated by Django 2.0 on 2018-04-23 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyMusic', '0003_action'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='photo',
            field=models.ImageField(null=True, upload_to='artists_photo/'),
        ),
    ]
