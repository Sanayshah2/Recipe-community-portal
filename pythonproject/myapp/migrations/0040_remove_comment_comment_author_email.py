# Generated by Django 3.0.3 on 2020-05-02 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0039_delete_subscriber'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='comment_author_email',
        ),
    ]