# Generated by Django 3.1.3 on 2020-11-21 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_auto_20201121_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.TextField(),
        ),
    ]