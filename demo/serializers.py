from rest_framework import serializers
from .models import Post
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

# serializer 类需要继承 serializers.Serializer，
# 然后实现父类的 update，create 方法
# validdata 的用法！！！
# class PostSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=70)
#     body = serializers.CharField()
#     create_time = serializers.DateTimeField(required=False)
#     modified_time = serializers.DateTimeField(required=False)
#     excerpt = serializers.CharField(max_length=200, allow_blank=True)
#
#     # 定义创建方法
#     def create(self, validated_date):
#         return Post.objects.create(**validated_date)
#
#     # 定义修改方法
#     def update(self, instance, validated_date):
#         instance.title = validated_date.get('title', instance.title)
#         instance.body = validated_date.get('body', instance.body)
#         instance.create_time = validated_date.get('create_time', instance.create_time)
#         instance.modified_time = validated_date.get('modified_time', instance.modified_time)
#         instance.excerpt = validated_date.get('excerpt', instance.excerpt)
#         instance.save()
#         return instance

class PostSerializer(serializers.ModelSerializer):
   class Meta:
       model = Post
       # result 接口需要返回的字段，可以指定 "__all__" 展示全部参数
       fields = ['title', 'body', 'create_time', 'modified_time', 'excerpt']
