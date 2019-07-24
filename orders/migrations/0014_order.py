# Generated by Django 2.2.3 on 2019-07-24 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_pizza_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal_size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meal_size', to='orders.Size')),
                ('meal_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meal_type', to='orders.Meal_Type')),
            ],
        ),
    ]