from django.urls import path
# from .views import helloAPI, signupAPI
from .views import signupAPI

urlpatterns = [
    # path("hello/", helloAPI),
    path("signup_cud/", signupAPI, name='signup_cud'),
]