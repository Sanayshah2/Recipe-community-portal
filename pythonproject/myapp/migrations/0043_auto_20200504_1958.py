# Generated by Django 3.0.3 on 2020-05-04 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0042_auto_20200504_1847'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='visits',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Count',
        ),
    ]