# Generated by Django 2.2.3 on 2019-07-23 14:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_delete_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='price',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
