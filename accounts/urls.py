from django.urls import path

from accounts.views import RegistrationAPIView

urlpatterns = [
    path('registration/', RegistrationAPIView.as_view()),
]
