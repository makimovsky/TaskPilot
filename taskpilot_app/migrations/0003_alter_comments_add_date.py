# Generated by Django 5.1.2 on 2024-10-09 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskpilot_app', '0002_workers_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='add_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]