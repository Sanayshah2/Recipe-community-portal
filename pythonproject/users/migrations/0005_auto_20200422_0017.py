# Generated by Django 3.0.2 on 2020-04-21 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200418_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank='true', choices=[('Male', 'Male'), ('Other', 'Other'), ('Female', 'Female')], default='', max_length=10, null='true'),
        ),
    ]
