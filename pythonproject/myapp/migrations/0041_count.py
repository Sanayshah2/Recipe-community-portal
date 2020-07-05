# Generated by Django 3.0.3 on 2020-05-04 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0040_remove_comment_comment_author_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Count',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visit_count', models.IntegerField()),
                ('food', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='myapp.Food')),
            ],
        ),
    ]
