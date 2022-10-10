from rest_framework.serializers import HyperlinkedModelSerializer, StringRelatedField
from rest_framework.serializers import ModelSerializer

from .models import Project, TodoProject


class ProjectModelSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class TodoProjectModelSerializer(ModelSerializer):
    class Meta:
        model = TodoProject
        fields = '__all__'
