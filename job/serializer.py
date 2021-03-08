from .models import Job
from rest_framework import serializers  # , viewsets


class Job_Serializer(serializers.ModelSerializer):
    class Meta:            
        model=Job
        fields='__all__'


