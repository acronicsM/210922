from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.decorators import api_view, renderer_classes


from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .serializers import UserModelSerializer
from .models import User


class UserAPIVIew(APIView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def get(self, request, format=None):
        pk = request.query_params.get('pk')
        users = User.objects.all()
        if pk:
            users = users.filter(id=pk)

        serializer = UserModelSerializer(users, many=True)
        return Response(serializer.data)


    def patch(self, request, format=None):
        pk = request.query_params.get('pk')
        if pk:
            users = User.objects.get(id=pk)
            if users:
                serializer = UserModelSerializer(users, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=HTTP_201_CREATED)

        return Response(status=HTTP_400_BAD_REQUEST)

