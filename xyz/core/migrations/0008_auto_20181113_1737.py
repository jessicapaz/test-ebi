# Generated by Django 2.1.3 on 2018-11-13 17:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20181113_1716'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productservice',
            old_name='commission',
            new_name='commission_rate',
        ),
        migrations.AlterField(
            model_name='sale',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 13, 17, 37, 25, 573624, tzinfo=utc)),
        ),
    ]
