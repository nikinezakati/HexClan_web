# Generated by Django 3.1.7 on 2021-05-13 12:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Lyrics', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='liked_section',
            name='likes',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='liked_section',
            name='lyric',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Lyrics.lyrics'),
        ),
        migrations.AddField(
            model_name='commented_section',
            name='lyric',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Lyrics.lyrics'),
        ),
        migrations.AddField(
            model_name='commented_section',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]