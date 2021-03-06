# Generated by Django 2.1.3 on 2018-11-14 16:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20181114_1316'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='email',
            field=models.EmailField(default='', max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='person',
            name='cpf',
            field=models.CharField(max_length=11, unique=True),
        ),
        migrations.AlterField(
            model_name='sale',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 14, 16, 11, 29, 155644, tzinfo=utc)),
        ),
    ]
