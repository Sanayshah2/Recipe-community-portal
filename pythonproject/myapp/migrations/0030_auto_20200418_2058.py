# Generated by Django 3.0.2 on 2020-04-18 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0029_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(default='', upload_to='category'),
        ),
        migrations.AlterField(
            model_name='food',
            name='image',
            field=models.ImageField(default='', upload_to='food'),
        ),
    ]
