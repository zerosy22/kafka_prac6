from django.db import models

# Create your models here.
class Signup(models.Model):
    SETBX_ID = models.IntegerField(primary_key=True)
    USER_EMAIL = models.CharField(max_length=100)
    USER_PWD = models.CharField(max_length=100)
    USER_NAME = models.CharField(max_length=50)
    USER_PHONE = models.CharField(max_length=50)
    user_sex = models.CharField(max_length=10)
    USER_BIRTH = models.DateField()
    USER_ADULT = models.CharField(max_length=10)
    USER_ADULT_KEY = models.CharField(max_length=20)
    USER_LIKE_GENRE = models.CharField(max_length=100)
    USER_LIKE_VOD = models.CharField(max_length=100)
    # user_sex = models.TextField()