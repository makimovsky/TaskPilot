from taskpilot_app import serializers
from taskpilot_app import models
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.parsers import JSONParser


class WorkersViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.WorkersSerializer
    queryset = models.Workers.objects.all()



