from django import db
from django.test import TestCase
#

# Create your tests here.
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
from mixer.backend.django import mixer
from django.contrib.auth.models import User

from .views import ProjectAPIView, TodoProjectAPIView
from .models import Project, TodoProject


class TestProjectViewSet(TestCase):

    def setUp(self) -> None:
        self.url = '/api/project'
        self.projects_dict = {'name': 'Project1', 'link': 'Project1.Projects.com', 'users': [1, 2]}
        self.projects_dict_fake = {'name': 'Project2', 'link': 'Project2.Projects.com', 'users': [3]}
        self.format = 'json'
        self.login = 'admin2@admin2.com'
        self.password = 'admin2'
        self.admin = User.objects.create_superuser(self.login, self.login, self.password)
        self.projects = Project.objects.create(**self.projects_dict)


    def test_factory_get_list(self):
        factory = APIRequestFactory()
        request = factory.get(self.url)
        view = ProjectAPIView.as_view({'get': 'get'})
        response = view(request)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_factory_create_guest(self):
        factory = APIRequestFactory()
        request = factory.post(self.url,self.projects_dict,format=self.format)
        view = ProjectAPIView.as_view({'post': 'post'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_factory_create_admin(self):
        factory = APIRequestFactory()
        request = factory.post(self.url,self.projects_dict,format=self.format)
        force_authenticate(request,self.admin)
        view = ProjectAPIView.as_view({'post':'post'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_api_client_detail(self):
        # APIClient
        client = APIClient()
        response = client.get(f'{self.url}{self.projects.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_client_update_guest(self):
        client = APIClient()
        response = client.put(f'{self.url}{self.projects.id}/',**self.projects_dict_fake)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_api_client_update_admin(self):
        client = APIClient()
        client.force_authenticate(user=self.admin)
        response = client.put(f'{self.url}{self.projects.id}/',
                              self.projects_dict_fake,format=self.format)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.projects.refresh_from_db()
        self.assertEqual(self.projects.name, self.projects_dict_fake.get('name'))
        self.assertEqual(self.projects.link, self.projects_dict_fake.get('link'))
        self.assertEqual(self.projects.users, self.projects_dict_fake.get('users'))
        client.logout()

    def tearDown(self) -> None:
        pass


class TestTodo(APITestCase):
    def setUp(self) -> None:
        self.url = '/api/todo/'
        self.projects_dict = {'name': 'Project1', 'link': 'Project1.Projects.com', 'users': [1, 2]}
        self.projects_dict_fake = {'name': 'Project2', 'link': 'Project2.Projects.com', 'users': [3]}
        self.format = 'json'
        self.projects = Project.objects.create(**self.projects_dict)
        self.projects_new = Project.objects.create(**self.projects_dict_fake)
        self.todo_dict = {'text': 'Test', 'project':self.projects}
        self.todo_dict_fake = {'text': 'change text', 'project': self.projects_new.id}
        self.todos = TodoProject.objects.create(**self.todo_dict)

    def test_api_test_case_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_api_test_case_update_admin(self):
        admin = User.objects.create_superuser('admin2', 'admin2@admin2.com','admin2')

        self.client.login(username='admin2', password='admin2')
        response = self.client.put(f'{self.url}{self.todos.id}/', self.todo_dict_fake)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

        self.todos.refresh_from_db()
        self.assertEqual(self.todos.text,self.todo_dict_fake.get('text'))
        self.assertEqual(self.todos.author.id,self.todo_dict_fake.get('project'))
        self.client.logout()



    def test_mixer(self):
        bio = mixer.blend(Project,text='DEVELOPER')
        self.client.force_authenticate(user=self.admin)

        response = self.client.put(f'{self.url}{bio.id}/', self.todo_dict_fake)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        bio.refresh_from_db()
        self.assertEqual(bio.text, self.todo_dict_fake.get('text'))
        self.assertEqual(bio.author.id, self.todo_dict_fake.get('project'))
        self.client.logout()

    def tearDown(self) -> None:
        pass