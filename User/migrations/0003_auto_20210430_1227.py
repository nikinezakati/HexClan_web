# Generated by Django 3.1.7 on 2021-04-30 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_auto_20210430_1156'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='avatar',
            new_name='avatar_pic',
        ),
    ]