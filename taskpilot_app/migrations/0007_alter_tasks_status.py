# Generated by Django 5.1.2 on 2024-10-16 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskpilot_app', '0006_remove_comments_task_id_comments_project_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='status',
            field=models.CharField(choices=[('not started', 'Not Started'), ('in progress', 'In Progress'), ('finished', 'Finished')], default='not started', max_length=30),
        ),
    ]