# Generated by Django 2.2.3 on 2019-07-25 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0022_auto_20190725_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='size',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='orders.Size'),
        ),
    ]