# Generated by Django 4.1.4 on 2022-12-19 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='completed',
            field=models.BooleanField(default=False, verbose_name=False),
            preserve_default=False,
        ),
    ]