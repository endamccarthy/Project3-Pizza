# Generated by Django 2.2.3 on 2019-08-14 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0056_remove_item_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]