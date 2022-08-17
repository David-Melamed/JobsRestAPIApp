from rest_framework import serializers
from .models import all_jobs


class JobsSerializer(serializers.ModelSerializer):
    class Meta:
        model = all_jobs
        fields = '__all__'
