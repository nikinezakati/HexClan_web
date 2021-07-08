# Generated by Django 3.1.7 on 2021-06-11 12:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commented_Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_index', models.IntegerField()),
                ('end_index', models.IntegerField()),
                ('context', models.CharField(default='', max_length=255)),
                ('date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Liked_Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_index', models.IntegerField()),
                ('end_index', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='lyrics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('music_id', models.CharField(default='', max_length=255)),
                ('context', models.JSONField()),
            ],
        ),
    ]
