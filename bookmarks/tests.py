from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from bookmarks.models import Bookmark

User = get_user_model()


class TestBookmarks(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            email='test@test.com',
            password='test1test1test1'
        )

        cls.bookmark = Bookmark.objects.create(
            user=cls.user,
            title='bookmark_1',
            description='description',
            url='http://127.0.0.1:8000/admin/',
            url_type='website',
        )

    def setUp(self):
        self.client.force_authenticate(user=self.user)

    def test_get_bookmark(self):
        url = reverse('bookmark', args=[self.bookmark.id])
        response = self.client.get(url)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
