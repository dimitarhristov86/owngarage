# Generated by Django 4.1 on 2022-09-12 19:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garage', '0010_alter_car_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 12, 22, 53, 29, 915698)),
        ),
    ]
