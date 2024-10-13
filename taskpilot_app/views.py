from taskpilot_app import serializers
from taskpilot_app import models
from rest_framework import viewsets
from rest_framework import filters
from django.shortcuts import render


class WorkersViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.WorkersSerializer
    queryset = models.Workers.objects.all()


class ClientsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ClientsSerializer
    queryset = models.Clients.objects.all()


class ProjectsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ProjectsSerializer
    queryset = models.Projects.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'description')


class TasksViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TasksSerializer
    queryset = models.Tasks.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'description')


class CommentsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CommentsSerializer
    queryset = models.Comments.objects.all()
