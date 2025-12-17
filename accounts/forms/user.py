from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from accounts.models import User as UserModel

User: type[UserModel] = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model: type[User] = User
        fields: tuple = ('email',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model: type[User] = User
        fields: tuple = ('email',)
