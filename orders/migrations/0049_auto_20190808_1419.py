# Generated by Django 2.2.3 on 2019-08-08 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0048_auto_20190808_1412'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='user',
            new_name='author',
        ),
    ]