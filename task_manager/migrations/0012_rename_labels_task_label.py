# Generated by Django 4.0.6 on 2022-08-26 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0011_alter_attachlabeltotask_attach_label_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='labels',
            new_name='label',
        ),
    ]