# Generated by Django 2.0.1 on 2020-01-24 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0020_auto_20190904_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='cursorlog',
            name='trial_to_down',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='cursorlog',
            name='trial_to_up',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
