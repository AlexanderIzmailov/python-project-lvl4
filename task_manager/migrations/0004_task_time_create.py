# Generated by Django 4.0.6 on 2022-08-17 10:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0003_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
