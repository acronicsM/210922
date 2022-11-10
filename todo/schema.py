import graphene
from graphene_django import DjangoObjectType
from todo_m.models import Project, User


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'


class Query(graphene.ObjectType):

    all_projects = graphene.List(ProjectType)
    all_users = graphene.List(UserType)

    def resolve_all_projects(root,info):
        return Project.objects.all()

    def resolve_all_users(root,info):
        return User.objects.all()


schema = graphene.Schema(query=Query)
