# Generated by Django 2.0.1 on 2019-06-17 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0009_userlog'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userlog',
            old_name='random',
            new_name='random_rate',
        ),
    ]