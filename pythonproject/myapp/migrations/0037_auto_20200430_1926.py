# Generated by Django 3.0.3 on 2020-04-30 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0036_subscriber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriber',
            name='email',
            field=models.EmailField(default='', max_length=254, null='False'),
        ),
    ]
