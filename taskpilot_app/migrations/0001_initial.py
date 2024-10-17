# Generated by Django 5.1.2 on 2024-10-17 14:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('client_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Workers',
            fields=[
                ('worker_id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('project_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=1000)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taskpilot_app.clients')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taskpilot_app.workers')),
            ],
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('task_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=1000)),
                ('status', models.CharField(choices=[('not started', 'Not Started'), ('in progress', 'In Progress'), ('finished', 'Finished')], default='not started', max_length=30)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taskpilot_app.projects')),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taskpilot_app.workers')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('comment_id', models.AutoField(primary_key=True, serialize=False)),
                ('comment', models.CharField(max_length=1000)),
                ('add_date', models.DateField(auto_now_add=True)),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taskpilot_app.projects')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taskpilot_app.workers')),
            ],
        ),
    ]
