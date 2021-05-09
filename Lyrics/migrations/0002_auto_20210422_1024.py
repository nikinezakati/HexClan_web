# Generated by Django 3.1.7 on 2021-04-22 10:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Lyrics', '0001_initial'),
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
