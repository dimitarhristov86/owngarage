# Generated by Django 4.1 on 2022-08-25 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('garage', '0004_car_image_alter_car_fuel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='car',
            options={'ordering': ['make']},
        ),
    ]
