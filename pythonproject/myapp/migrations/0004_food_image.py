# Generated by Django 3.0.3 on 2020-03-28 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='image',
            field=models.ImageField(default='', upload_to='myapp/images'),
        ),
    ]
