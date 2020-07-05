# Generated by Django 3.0.2 on 2020-04-26 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0034_auto_20200426_2359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.CharField(default='Anonymous', max_length=30, null='False'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(null='False'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_author_email',
            field=models.EmailField(default='Anonymous', max_length=254, null='False'),
        ),
    ]
