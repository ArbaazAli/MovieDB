# Generated by Django 3.1.3 on 2020-11-23 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0007_auto_20201121_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='duration',
            field=models.TimeField(),
        ),
    ]