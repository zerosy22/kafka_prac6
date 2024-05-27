from rest_framework import serializers
from .models import Signup

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signup
        fields = ['SETBX_ID', 'USER_EMAIL', 'USER_PWD', 
                'USER_NAME', 'USER_PHONE', 'user_sex',
                'USER_BIRTH ', 'USER_ADULT', 'USER_ADULT_KEY',
                'USER_LIKE_GENRE', 'USER_LIKE_VOD',]