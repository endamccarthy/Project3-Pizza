# Generated by Django 2.2.3 on 2019-07-26 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0035_remove_size_meal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='meal_addition',
            field=models.ManyToManyField(blank=True, to='orders.Meal_Addition'),
        ),
    ]
