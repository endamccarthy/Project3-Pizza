# Generated by Django 2.2.3 on 2019-07-26 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0029_auto_20190725_1551'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meal_addition',
            name='meal_type',
        ),
        migrations.AddField(
            model_name='meal_type',
            name='meal_addition',
            field=models.ManyToManyField(to='orders.Meal_Addition'),
        ),
    ]
