from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Signup
from .serializers import SignupSerializer
from rest_framework import status

import mysql.connector

# @api_view(['GET'])
# def helloAPI(request):
#     return Response("hello world!")

@api_view(['POST'])
def signupAPI(request):
    data = request.data
    # print(data)
    # Check for existing SETBX_ID in Django model
    if Signup.objects.filter(SETBX_ID=data.get('SETBX_ID')).exists():
        return Response({"error": "signup with this SETBX ID already exists."}, status=status.HTTP_400_BAD_REQUEST)

    # Save to Django model
    serializer = SignupSerializer(data=data)
    if serializer.is_valid():
        serializer.save()

        try:
            # MySQL 데이터베이스에 연결
            conn = mysql.connector.connect(
                host='dbmysqluser.cfko8844sqv2.ap-northeast-2.rds.amazonaws.com',
                user='admin_user',
                password='user0409',
                database='db_user'
            )
            cursor = conn.cursor()

            # 데이터 삽입 쿼리
            query = """
            INSERT INTO mysql_user (
                SETBX_ID, USER_EMAIL, USER_PWD, USER_NAME, USER_PHONE, USER_SEX, 
                USER_BIRTH, USER_ADULT, USER_ADULT_KEY, USER_LIKE_GENRE, USER_LIKE_VOD
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            values = (
                data['SETBX_ID'], data['USER_EMAIL'], data['USER_PWD'], data['USER_NAME'],
                data['USER_PHONE'], data['user_sex'], data['USER_BIRTH'], data['USER_ADULT'],
                data['USER_ADULT_KEY'], data['USER_LIKE_GENRE'], data['USER_LIKE_VOD']
            )

            # 쿼리 실행
            cursor.execute(query, values)
            conn.commit()

            return Response({"message": "Data inserted successfully"}, status=status.HTTP_201_CREATED)
        except mysql.connector.Error as err:
            return Response({"error": str(err)}, status=status.HTTP_400_BAD_REQUEST)
        finally:
            cursor.close()
            conn.close()
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)