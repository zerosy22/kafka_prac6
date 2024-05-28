from django.apps import AppConfig

import pymysql
from pymongo import MongoClient 
from datetime import datetime

class ReadappConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "readapp"
    def ready(self):
        print("시작하자 마자 한 번만 수행")
        #데이터베이스 연결
        con = pymysql.connect(host='dbmysqluser.cfko8844sqv2.ap-northeast-2.rds.amazonaws.com', 
                              port=3306, 
                              user='admin_user', 
                              passwd='user0409',
                              db='db_user',
                              charset ='utf8')
        #데이터베이스 연결
        # conn = conn = MongoClient('mongodb://bbanggoood_db_mongo:bbanggoood0409@3.39.109.134' % ("bbanggoood_db_mongo", "bbanggoood0409"))
        conn = conn = MongoClient('mongodb://bbanggoood_db_mongo:bbanggoood0409@3.39.109.134:27017/?authSource=db_mongo')
        
        #데이터베이스 설정
        db = conn.db_mongo
        #컬렉션 설정
        collect = db.user
        collect.delete_many({})

        cursor = con.cursor()

 	    # 데이터 읽어오는 SQL 실행
        cursor.execute("select * from mysql_user")
        # 전체 데이터를 가져와서 튜플의 튜플로 생성
        data = cursor.fetchall()
        for imsi in data:
            date = imsi[6].strftime("%Y-%m-%d")
            doc = {'bid':imsi[0], 'title':imsi[1], 
                   'author':imsi[2], 'category':imsi[3],
                   'pages':imsi[4], 'price':imsi[5], 
                   'published_date':date, 'description':imsi[7]}
            collect.insert_one(doc)

        con.close()
