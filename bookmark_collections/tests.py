from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

User = get_user_model()


class TestBookmarks(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            email='test@test.com',
            password='test1test1test1'
        )

        cls.data = {
            'title': 'collection_1',
            'description': 'description'
        }

    def setUp(self):
        self.client.force_authenticate(user=self.user)

    def test_add_collection(self):
        url = reverse('collections')
        response = self.client.post(url, data=self.data)

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
