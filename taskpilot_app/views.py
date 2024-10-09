from taskpilot_app import serializers
from taskpilot_app import models
from rest_framework import viewsets
from rest_framework import filters
from django.shortcuts import render


def project_list(request):
    queryset = models.Projects.objects.all()
    return render(request, 'project_list.html', {'projects': queryset})


def worker_list(request):
    queryset = models.Workers.objects.all()
    return render(request, 'worker_list.html', {'workers': queryset})


def client_list(request):
    queryset = models.Clients.objects.all()
    return render(request, 'client_list.html', {'clients': queryset})


def main(request):
    return render(request, 'app.html')


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
