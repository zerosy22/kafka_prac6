from django.db import models

# Create your models here.
class Signup(models.Model):
    SETBX_ID = models.IntegerField(primary_key=True)
    USER_EMAIL = models.CharField(max_length=255, unique=True)
    USER_PWD = models.CharField(max_length=255)
    USER_NAME = models.CharField(max_length=100)
    USER_PHONE = models.CharField(max_length=20)
    user_sex = models.CharField(max_length=255)
    USER_BIRTH = models.DateField()
    USER_ADULT = models.BooleanField(default=False)
    USER_ADULT_KEY = models.CharField(max_length=4, null=True, blank=True)
    USER_LIKE_GENRE = models.CharField(max_length=255, null=True, blank=True)
    USER_LIKE_VOD = models.CharField(max_length=255, null=True, blank=True)
    USER_ROLE = models.CharField(max_length=10, choices=[('ROLE_ADMIN', 'ROLE_ADMIN')], default='ROLE_ADMIN')
    USER_CREATED_AT = models.DateTimeField(auto_now_add=True)
    USER_UPDATED_AT = models.DateTimeField(auto_now=True)
    confirm_user_pwd = models.CharField(max_length=255, null=True, blank=True)