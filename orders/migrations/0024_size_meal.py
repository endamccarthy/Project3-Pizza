# Generated by Django 2.2.3 on 2019-07-25 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0023_order_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='size',
            name='meal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Meal'),
        ),
    ]
