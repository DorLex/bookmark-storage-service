from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from accounts.models import User as UserModel
from bookmarks.models import Bookmark
from core.enums.url import UrlTypeChoices

User: type[UserModel] = get_user_model()


class TestBookmarks(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.user: User = User.objects.create_user(
            email='user_1@test.com',
            password='password_user_1',
        )

        cls.bookmark: Bookmark = Bookmark.objects.create(
            user=cls.user,
            title='bookmark_1',
            description='description_bookmark_1',
            url='http://127.0.0.1:8000/admin/',
            url_type=UrlTypeChoices.website,
        )

    def setUp(self) -> None:
        self.client.force_authenticate(user=self.user)

    def test_get_bookmark(self) -> None:
        url: str = reverse('bookmark-detail', args=[self.bookmark.pk])
        response: Response = self.client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert response.data['title'] == self.bookmark.title
        assert response.data['url'] == self.bookmark.url

    def test_partial_update_bookmark(self) -> None:
        url: str = reverse('bookmark-detail', args=[self.bookmark.pk])
        new_title: str = 'updated_title'
        body: dict = {'title': new_title}
        response: Response = self.client.patch(url, data=body)

        assert response.status_code == status.HTTP_200_OK
        assert response.data['title'] == new_title
        assert response.data['url'] == self.bookmark.url

    def test_delete_bookmark(self) -> None:
        url: str = reverse('bookmark-detail', args=[self.bookmark.pk])
        response: Response = self.client.delete(url)

        assert response.status_code == status.HTTP_200_OK
