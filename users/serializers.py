from rest_framework.serializers import ModelSerializer

from .models import User


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'second_name', 'age', 'email', 'is_active')


class UserFullModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'