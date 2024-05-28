from django.urls import path
from .views import signupAPI

urlpatterns = [
    path("signup_r/", signupAPI),
]
