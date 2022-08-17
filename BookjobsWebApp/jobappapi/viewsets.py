from rest_framework import viewsets
from . import models
from . import serializers


class JobsViewset(viewsets.ModelViewSet):
    queryset = models.all_jobs.objects.all()
    serializer_class = serializers.JobsSerializer
