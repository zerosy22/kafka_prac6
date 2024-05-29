from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Signup
from .serializers import SignupSerializer
from rest_framework import status

import mysql.connector

from kafka import KafkaProducer
import json


class MessageProducer:
    def __init__(self, broker, topic):
        self.broker = broker
        self.topic = topic
        #key_serializer=str.encode 를 추가하면 key 와 함께 전송 
        #그렇지 않으면 value 만 전송
        self.producer = KafkaProducer(
            bootstrap_servers=self.broker,
            value_serializer=lambda x: json.dumps(x).encode("utf-8"),
            acks=0,
            api_version=(2, 5, 0),
            key_serializer=str.encode,
            retries=3,
        )
    def send_message(self, msg, auto_close=True):
        try:
            print(self.producer)
            future = self.producer.send(self.topic, value=msg, key="key")
            self.producer.flush()  # 비우는 작업
            if auto_close:
                self.producer.close()
            future.get(timeout=2)
            return {"status_code": 200, "error": None}
        except Exception as exc:
            raise exc



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
        # 브로커와 토픽명을 지정
        broker = ["43.203.228.94:9092"]
        # AWS EC2 kafka 인스턴스 spec:t2.medium
        topic = "usertopic"
        pd = MessageProducer(broker, topic)
        #전송할 메시지 생성
        msg = {"task": "insert", "data": serializer.data}
        res = pd.send_message(msg)
        print(res)

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