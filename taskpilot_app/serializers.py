from rest_framework import serializers
from taskpilot_app import models


class WorkersSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Workers
        fields = ('worker_id', 'email', 'name', 'surname')


class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Clients
        fields = ('client_id', 'name', 'email')


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Projects
        fields = ('project_id', 'client', 'name', 'description')


class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tasks
        fields = ('task_id', 'project_id', 'worker', 'name', 'description', 'status', 'start_date', 'end_date')


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comments
        fields = ('comment_id', 'project_id', 'author', 'comment', 'add_date')
