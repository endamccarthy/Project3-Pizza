# Generated by Django 2.2.3 on 2019-07-25 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0025_auto_20190725_1417'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meal_type',
            name='size',
        ),
        migrations.AddField(
            model_name='size',
            name='meal',
            field=models.ManyToManyField(to='orders.Meal'),
        ),
    ]
