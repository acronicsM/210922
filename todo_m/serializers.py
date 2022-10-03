from rest_framework.serializers import HyperlinkedModelSerializer, StringRelatedField

from .models import Project, TodoProject


class ProjectModelSerializer(HyperlinkedModelSerializer):
    # users = StringRelatedField(many=True)
    class Meta:
        model = Project
        fields = '__all__'


class TodoProjectModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = TodoProject
        fields = '__all__'
