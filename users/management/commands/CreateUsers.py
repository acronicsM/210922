from django.core.management.base import BaseCommand
import django.contrib.auth

class Command(BaseCommand):
    help = 'The Zen of Python'

    def handle(self, *args, **options):
        User = django.contrib.auth.get_user_model()
        user = User.objects.create_user('super101', password='Qwerty!@#$%^', email='super@super.local')
        user.is_superuser = True
        user.is_staff = True
        user.save()

        for i in range(5):
            name = f'test{i}'
            user = User.objects.create_user(name, password=name.capitalize(), email=f'{name}@test.local')
            user.save()

