# Generated by Django 4.0.6 on 2022-08-19 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0009_rename_label_attachlabeltotask_attach_label_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachlabeltotask',
            name='attach_label',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='task_manager.task'),
        ),
        migrations.AlterField(
            model_name='attachlabeltotask',
            name='attach_task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='task_manager.label'),
        ),
    ]
