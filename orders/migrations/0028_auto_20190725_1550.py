# Generated by Django 2.2.3 on 2019-07-25 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0027_auto_20190725_1437'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meal_Addition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('meal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Meal')),
                ('meal_type', models.ManyToManyField(to='orders.Meal_Type')),
            ],
        ),
        migrations.RemoveField(
            model_name='pizza',
            name='name',
        ),
        migrations.RemoveField(
            model_name='pizza',
            name='size',
        ),
        migrations.DeleteModel(
            name='Pizza_Topping',
        ),
        migrations.DeleteModel(
            name='Sub_Addition',
        ),
        migrations.DeleteModel(
            name='Pizza',
        ),
        migrations.AddField(
            model_name='order',
            name='meal_addition',
            field=models.ManyToManyField(null=True, to='orders.Meal_Addition'),
        ),
    ]
