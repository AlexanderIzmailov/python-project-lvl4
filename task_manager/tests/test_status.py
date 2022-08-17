from task_manager.models import Status
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


class TestStatus(TestCase):
    def setUp(self):
        self.client = Client()
        
        user = User.objects.create(username='test_user')
        user.set_password('12345')
        user.save()


    def test_creating_status(self):
        response = self.client.login(username='test_user', password='12345')
        response = self.client.post(reverse('statuses_create'), {
            'name': 'Status_1'
        })
        status = Status.objects.get(id=1)
        assert status.name == "Status_1"
    

    def test_updating_status(self):
        Status.objects.create(name='Status_1')
        response = self.client.login(username='test_user', password='12345')
        response = self.client.post(reverse('statuses_update', args=[1]), {
            'name': 'Status_2'
        })

        status = Status.objects.get(id=1)
        assert status.name == "Status_2"


    def test_deleting_status(self):
        Status.objects.create(name='Status_1')
        response = self.client.login(username='test_user', password='12345')
        response = self.client.post(reverse('statuses_delete', args=[1]))
        status_count = Status.objects.all().count()
        assert status_count == 0
    

    def test_acces_to_statuses_list_without_auth(self):
        response = self.client.get(reverse('statuses_list'))
        assert response.url == "/login/?next=/statuses/"
