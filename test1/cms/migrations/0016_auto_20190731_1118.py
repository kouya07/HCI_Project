# Generated by Django 2.0.1 on 2019-07-31 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0015_auto_20190726_1437'),
    ]

    operations = [
        migrations.AddField(
            model_name='userlog',
            name='end_time',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='userlog',
            name='start_time',
            field=models.CharField(max_length=20, null=True),
        ),
    ]