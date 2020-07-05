# Generated by Django 3.0.3 on 2020-04-13 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0028_auto_20200413_1310'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(default='Anonymous', max_length=30)),
                ('comment', models.TextField()),
                ('food', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='myapp.Food')),
            ],
        ),
    ]
