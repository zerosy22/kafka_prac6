from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from pymongo import MongoClient 
from bson import json_util
import json

@api_view(['GET'])
def signupAPI(request):
    # 데이터베이스 연결
    conn = MongoClient('mongodb://bbanggoood_db_mongo:bbanggoood0409@3.39.109.134:27017/?authSource=db_mongo')
    # 데이터베이스 설정
    db = conn.db_mongo
    # 컬렉션 설정
    collect = db.user 
    # 전체 문서 조회
    result = collect.find()
    # 조회 문서 출력
    data = []
    for r in result :
        print(type(r))
        data.append(r)

    return Response(json.loads(json_util.dumps(data)), status=status.HTTP_201_CREATED)
