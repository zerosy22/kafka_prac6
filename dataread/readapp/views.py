from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from pymongo import MongoClient 
from bson import json_util
import json

class MongoDBClient:
    def __init__(self, uri, db_name):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]

    def get_collection(self, collection_name):
        return self.db[collection_name]

# MongoDB 클라이언트 인스턴스 생성
mongodb_client = MongoDBClient('mongodb://bbanggoood_db_mongo:bbanggoood0409@3.39.109.134:27017/?authSource=db_mongo', 'db_mongo')

@api_view(['GET'])
def signupAPI(request):
    # 컬렉션 설정
    collect = mongodb_client.get_collection('user')
    # # 데이터베이스 설정
    # db = conn.cqrs
    # # 컬렉션 설정
    # collect = db.books
    # 전체 문서 조회
    result = collect.find()
    # 조회 문서 출력
    data = []
    for r in result:
        data.append(r)
    return Response(json.loads(json_util.dumps(data)), status=status.HTTP_200_OK)