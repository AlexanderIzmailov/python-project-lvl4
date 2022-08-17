from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse 


class TestUser(TestCase):
    def setUp(self):
        self.client = Client()

        user = User.objects.create(username='test_user', first_name="Alexander")
        user.set_password('12345')
        user.save()


    def test_creating_user(self):
        response = self.client.post(reverse('users_create'), {
            'username': 'AlIz',
            'first_name': 'Alexander',
            'last_name': 'Izmailov',
            'password1': 'pss12asddaSA',
            'password2': 'pss12asddaSA'
        })
        user = User.objects.get(id=2)
        assert user.username == "AlIz"
    

    # def test_access_to_update_another_user(self):
    #     user = User.objects.create(username='test_user_2')
    #     user.set_password('12345')
    #     user.save()

    #     response = self.client.login(username='test_user_2', password='12345')
    #     response = self.client.post(reverse('users_update', args=[1]), {
    #         'username': 'AlIz',
    #         'first_name': 'Alexander',
    #         'last_name': 'Izmailov',
    #         'password1': 'pss12asddaSA',
    #         'password2': 'pss12asddaSA'
    #     })
    #     print("AAAA", response)
    #     assert 1 == 1


    def test_updating_user(self):
        response = self.client.login(username='test_user', password='12345')
        
        response = self.client.post(reverse('users_update', args=[1]), {
            'username': 'AlIz',
            'first_name': 'Alexander',
            'last_name': 'Izmailov',
            'password1': 'pss12asddaSA',
            'password2': 'pss12asddaSA'
        })

        user = User.objects.get(id=1)
        assert user.first_name == "Alexander"


    def test_deleting_user(self):
        response = self.client.login(username='test_user', password='12345')
        response = self.client.post(reverse('users_delete', args=[1]))
        users = User.objects.all().count()
        assert users == 0
