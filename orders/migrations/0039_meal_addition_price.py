# Generated by Django 2.2.3 on 2019-07-27 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0038_auto_20190726_1050'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal_addition',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
