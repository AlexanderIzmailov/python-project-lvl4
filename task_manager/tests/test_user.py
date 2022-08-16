from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse 


class TestUser(TestCase):
    def setUp(self):
        self.client = Client()
        self.client.post(reverse('users_create'), {
            'username': 'AlIz',
            'first_name': 'Alexander',
            'last_name': 'Izmailov',
            'password1': 'pss12asddaSA',
            'password2': 'pss12asddaSA'
        })


    def test_creating_user(self):
        user = User.objects.get(id=1)
        assert user.username == "AlIz"
    

    def test_updating_user(self):
        response = self.client.login(username='AlIz', password='pss12asddaSA')
        
        response = self.client.post(reverse('users_update', args=[1]), {
            'username': 'AlIz',
            'first_name': 'Alexander_2',
            'last_name': 'Izmailov',
            'password1': 'pss12asddaSA',
            'password2': 'pss12asddaSA'
        })

        user = User.objects.get(id=1)
        assert user.first_name == "Alexander_2"


    def test_deleting_user(self):
        response = self.client.login(username='AlIz', password='pss12asddaSA')
        response = self.client.post(reverse('users_delete', args=[1]))
        users = User.objects.all().count()
        assert users == 0
