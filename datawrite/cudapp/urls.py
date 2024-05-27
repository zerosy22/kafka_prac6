from django.urls import path
from .views import helloAPI, signupAPI

urlpatterns = [
    path("hello/", helloAPI),
    path("signup/", signupAPI),
]