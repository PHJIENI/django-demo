import json
import pprint
from io import BytesIO

from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView
from rest_framework.parsers import JSONParser, FormParser
from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView


from .models import Post
from .serializers import PostSerializer

# 通过url传参
@csrf_exempt
def getParamsFromUrl(request, pk):
    print(pk)
    return HttpResponse(pk)

# 基础写法：Post请求，Vue侧传FormData类型的参数
@csrf_exempt
def post_list(request):
   # 如果是 GET 请求则返回所有的列表
   if request.method == "GET":
       posts = Post.objects.all()
       serializer = PostSerializer(posts, many=True)
       return JsonResponse(serializer.data, safe=False)

   # 如果是 POST 请求则保存数据
   elif request.method == "POST":
       # 将 request 中的参数取出来进行序列化
       stream = BytesIO(request.body)
       data=FormParser().parse(stream)
       pprint.pprint(dict(data))
       serializer = PostSerializer(data=data)
        # 判断是否有效的数据
       if serializer.is_valid():
           # 有效数据保存，返回 201 CREATED
           serializer.save()
           return JsonResponse(serializer.data, status=201)
       # 无效则返回 400 BAD_REQUEST
       return JsonResponse(serializer.errors, status=400)

# 引入api_view的写法
@api_view(['GET', 'POST'])
def api_view_post_list(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        # 通过 Response 展示相应的数据
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # 引入 status 模块，比数字标识符更加直观
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostList(APIView):
    # 定义 GET 请求的方法，内部实现相同 @api_view
    def get(self, request, format=None):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 定义 POST 请求的方法
    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)