# Generated by Django 3.1.7 on 2021-04-05 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Page', '0001_initial'),
        ('User', '0002_auto_20210401_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='album_ratings',
            field=models.ManyToManyField(blank=True, null=True, related_name='user_albumrating', to='Page.Album'),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=None),
        ),
        migrations.AlterField(
            model_name='user',
            name='description',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='favorites_albums',
            field=models.ManyToManyField(blank=True, null=True, to='Page.Album'),
        ),
        migrations.AlterField(
            model_name='user',
            name='favorites_artists',
            field=models.ManyToManyField(blank=True, null=True, to='Page.Artist'),
        ),
        migrations.AlterField(
            model_name='user',
            name='favorites_musics',
            field=models.ManyToManyField(blank=True, null=True, related_name='user_favoritemusic', to='Page.Music'),
        ),
        migrations.AlterField(
            model_name='user',
            name='music_ratings',
            field=models.ManyToManyField(blank=True, null=True, to='Page.Music'),
        ),
    ]
