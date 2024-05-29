from django.apps import AppConfig

import pymysql
from pymongo import MongoClient 
from datetime import datetime

# import sys
# import six
# if sys.version_info >= (3, 12, 0): 
#     sys.modules['kafka.vendor.six.moves'] = six.moves

from kafka import KafkaConsumer
import threading
import json


class MessageConsumer:
    def __init__(self, broker, topic, mongo_uri):
        self.broker = broker
        self.mongo_uri = mongo_uri
        self.consumer = KafkaConsumer(
            topic,  # Topic to consume
            bootstrap_servers=self.broker,
            value_deserializer=lambda x: x.decode(
                "utf-8"
            ),  # Decode message value as utf-8
            group_id="my-group",  # Consumer group ID
            auto_offset_reset="earliest",  # Start consuming from earliest available message
            enable_auto_commit=True,  # Commit offsets automatically
        )
        

    def receive_message(self):
        try:
            for message in self.consumer:
                if not message.value:
                    print("Empty message received")
                    continue

                try:
                    result = json.loads(message.value)
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON: {e}")
                    continue

                imsi = result["data"]          
                doc = {
                    'SETBX_ID': imsi["SETBX_ID"],
                    'USER_EMAIL': imsi["USER_EMAIL"],
                    'USER_PWD': imsi["USER_PWD"],
                    'USER_NAME': imsi["USER_NAME"],
                    'USER_PHONE': imsi["USER_PHONE"],
                    'user_sex': imsi["user_sex"],
                    'USER_BIRTH': imsi["USER_BIRTH"],
                    'USER_ADULT': imsi["USER_ADULT"],
                    'USER_ADULT_KEY': imsi["USER_ADULT_KEY"],
                    'USER_LIKE_GENRE': imsi["USER_LIKE_GENRE"],
                    'USER_LIKE_VOD': imsi["USER_LIKE_VOD"],
                    'USER_ROLE': imsi["USER_ROLE"],
                    'USER_CREATED_AT': imsi["USER_CREATED_AT"],
                    'USER_UPDATED_AT': imsi["USER_UPDATED_AT"],
                    'confirm_user_pwd': imsi["confirm_user_pwd"]
                }
                # MongoDB에 데이터 삽입
                # 데이터베이스 연결
                conn = MongoClient(self.mongo_uri)
                # conn = MongoClient('mongodb://bbanggoood_db_mongo:bbanggoood0409@3.39.109.134:27017/?authSource=db_mongo')
                # conn = MongoClient('mongodb://%s:%s@3.34.125.24' % ("myUseradmin", "wnddkd"))
                # 데이터베이스 설정
                db = conn.db_mongo
                # 컬렉션 설정
                collect = db.user
                collect.insert_one(doc)
                print(doc)
                conn.close()
        except Exception as exc:
            print(f"Error in receive_message: {exc}")
            raise exc



class ReadappConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "readapp"

    def ready(self):
        print("시작하자 마자 한 번만 수행")
        self.init_mongo()
        self.init_mysql()
        self.start_kafka_consumer()


    def init_mongo(self):
        # MongoDB 데이터베이스 연결
        # conn = MongoClient('mongodb://bbanggoood_db_mongo:bbanggoood0409@3.39.109.134' % ("bbanggoood_db_mongo", "bbanggoood0409"))
        conn = MongoClient('mongodb://bbanggoood_db_mongo:bbanggoood0409@3.39.109.134:27017/?authSource=db_mongo')
        #데이터베이스 설정
        db = conn.db_mongo
        #컬렉션 설정
        collect = db.user
        collect.delete_many({})
        conn.close()



    def init_mysql(self):
        try:
            # MySQL 데이터베이스 연결
            con = pymysql.connect(
                host='dbmysqluser.cfko8844sqv2.ap-northeast-2.rds.amazonaws.com',
                port=3306,
                user='admin_user',
                passwd='user0409',
                db='db_user',
                charset='utf8'
            )

            cursor = con.cursor()
            # 데이터 읽어오는 SQL 실행
            cursor.execute("select * from mysql_user")
            # 전체 데이터를 가져와서 튜플의 튜플로 생성
            data = cursor.fetchall()

            conn = MongoClient('mongodb://bbanggoood_db_mongo:bbanggoood0409@3.39.109.134:27017/?authSource=db_mongo')
            db = conn.db_mongo
            collect = db.user

            for imsi in data:
                date = imsi[6].strftime("%Y-%m-%d")
                doc = {
                    'SETBX_ID': imsi[0],
                    'USER_EMAIL': imsi[1],
                    'USER_PWD': imsi[2],
                    'USER_NAME': imsi[3],
                    'USER_PHONE': imsi[4],
                    'user_sex': imsi[5],
                    'USER_BIRTH': date,
                    'USER_ADULT': imsi[7],
                    'USER_ADULT_KEY': imsi[8],
                    'USER_LIKE_GENRE': imsi[9],
                    'USER_LIKE_VOD': imsi[10],
                    'USER_ROLE': imsi[11],
                    'USER_CREATED_AT': imsi[12],
                    'USER_UPDATED_AT': imsi[13],
                    'confirm_user_pwd': imsi[14]
                }
                collect.insert_one(doc)

            con.close()


        except Exception as e:
            print(f"Error initializing MySQL to MongoDB: {e}")


    def start_kafka_consumer(self):
        # broker = ["localhost:9092"]
        broker = ["43.203.228.94:9092"]
        topic = "usertopic"
        mongo_uri = 'mongodb://bbanggoood_db_mongo:bbanggoood0409@3.39.109.134:27017/?authSource=db_mongo'
        consumer = MessageConsumer(broker, topic, mongo_uri)
        t = threading.Thread(target=consumer.receive_message)
        t.start()