# Generated by Django 3.1.7 on 2021-03-30 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hex_clan', '0007_artist_profie_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='profie_type',
        ),
        migrations.RemoveField(
            model_name='artist',
            name='profie_type',
        ),
        migrations.RemoveField(
            model_name='music',
            name='profie_type',
        ),
    ]
