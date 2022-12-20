# Generated by Django 4.1.4 on 2022-12-19 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_todolist_completed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todolist',
            name='tid',
        ),
        migrations.AlterField(
            model_name='todolist',
            name='completed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]