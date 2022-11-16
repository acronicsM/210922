from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.pagination import LimitOffsetPagination


from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .serializers import ProjectModelSerializer, TodoProjectModelSerializer
from .models import Project, TodoProject


class ProjectAPIView(APIView, LimitOffsetPagination):

    permission_classes = [AllowAny]

    def get(self, request, format=None):
        pk = request.query_params.get('pk')
        name = request.query_params.get('name')
        project = Project.objects.all()
        if pk:
            project = project.filter(id=pk)
        elif name:
            project = project.filter(name__contains=name)

        serializer = ProjectModelSerializer(project, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProjectModelSerializer(data=request.data, context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(status=HTTP_400_BAD_REQUEST)

    def patch(self, request, format=None):
        pk = request.query_params.get('pk')
        if pk:
            project = Project.objects.get(id=pk)
            if project:
                serializer = ProjectModelSerializer(project, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=HTTP_201_CREATED)

        return Response(status=HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        pk = request.query_params.get('pk')
        if pk:
            project = Project.objects.get(id=pk)
            if project:
                project.delete()
                projects = Project.objects.all()
                serializer = ProjectModelSerializer(projects, many=True)
                return Response(serializer.data)

        return Response(status=HTTP_400_BAD_REQUEST)


class TodoProjectAPIView(APIView):
    def get(self, request, format=None):
        pk = request.query_params.get('pk')
        project = request.query_params.get('project')
        todo = TodoProject.objects.all()
        if pk:
            todo = todo.filter(id=pk)
        elif project:
            todo = todo.filter(project=project)

        serializer = TodoProjectModelSerializer(todo, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TodoProjectModelSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        print(serializer.errors)
        return Response(status=HTTP_400_BAD_REQUEST)

    def patch(self, request, format=None):
        pk = request.query_params.get('pk')
        if pk:
            todo = TodoProject.objects.get(id=pk)
            if todo:
                serializer = TodoProjectModelSerializer(todo, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=HTTP_201_CREATED)

        return Response(status=HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        pk = request.query_params.get('pk')
        if pk:
            project = TodoProject.objects.get(id=pk)
            if project:
                project.activ = False
                project.save()

                serializer = TodoProjectModelSerializer(project)
                return Response(serializer.data)

        return Response(status=HTTP_400_BAD_REQUEST)
