# Generated by Django 2.2.3 on 2019-07-24 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0015_auto_20190724_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='pizza_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pizza_type', to='orders.Pizza_Type'),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pizza_type1', to='orders.Pizza_Type'),
        ),
    ]
