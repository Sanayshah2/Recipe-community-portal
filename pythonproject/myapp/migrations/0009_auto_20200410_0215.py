# Generated by Django 3.0.3 on 2020-04-09 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_food_ingredients'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='category',
            field=models.CharField(choices=[('Non veg', 'Non veg'), ('Veg', 'Veg'), ('North Indian', 'North Indian'), ('Chinese', 'Chinese'), ('Italian', 'Italian'), ('Spanish', 'Spanish'), ('American', 'American')], default='', max_length=30),
        ),
    ]