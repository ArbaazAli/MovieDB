# Generated by Django 3.1.3 on 2020-11-23 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0008_auto_20201123_1108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genre',
            name='movies',
        ),
        migrations.AddField(
            model_name='genre',
            name='movie',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='movies', to='movie.movie'),
            preserve_default=False,
        ),
    ]
