# Generated by Django 2.1.3 on 2018-11-13 17:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20181113_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 13, 17, 39, 8, 123468, tzinfo=utc)),
        ),
    ]
