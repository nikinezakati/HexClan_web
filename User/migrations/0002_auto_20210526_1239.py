# Generated by Django 3.1.7 on 2021-05-26 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='total_album_rating',
            name='artist_id',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='total_music_rating',
            name='artist_id',
            field=models.CharField(default='', max_length=255),
        ),
    ]
