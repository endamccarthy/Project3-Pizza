# Generated by Django 2.2.3 on 2019-07-25 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0028_auto_20190725_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='meal_addition',
            field=models.ManyToManyField(to='orders.Meal_Addition'),
        ),
    ]
