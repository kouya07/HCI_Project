# Generated by Django 2.0.1 on 2019-06-23 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0011_auto_20190623_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cursorlog',
            name='round',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
