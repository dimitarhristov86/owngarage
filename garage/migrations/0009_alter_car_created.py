# Generated by Django 4.1 on 2022-08-28 19:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garage', '0008_alter_car_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 28, 22, 53, 31, 24855)),
        ),
    ]
