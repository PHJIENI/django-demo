import sys
import os
import django
# 获取当前文件的目录


pwd = os.path.dirname(os.path.realpath(__file__))
# 获取当前项目名的目录(因为我的当前文件是在项目名下的文件夹下的文件.所以是../)
sys.path.append(r"C:\Users\Administrator\Desktop\django_practise\django_practise")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_demo.settings")
django.setup()
from demo.models import *
from demo.serializers import *

def create():
    """
    增
    """
    data = {'title': 'hello11111', 'body': 'hea', 'create_time': '2022-09-20T23:40:12.507826', 'modified_time': '2022-09-20T23:42:48.077658', 'excerpt': 'hell1'}
    serializer = PostSerializer(data=data)
    serializer.is_valid()
    serializer.save()

def select():
    """
    查
    """
    obj = Post.objects.get(id=1)
    serializer = PostSerializer(instance=obj)
    print(serializer.data)
    print(Post.objects.filter(id=1).values()[0])

def delete():
    Post.objects.get(id="").delete()

def update():
    data = {'title': 'hello11111', 'body': 'hea', 'create_time': '2022-09-20T23:40:12.507826',
            'modified_time': '2022-09-20 23:42:48.077658', 'excerpt': 'hell1'}
    serializer = PostSerializer(data=data)
    obj = Post.objects.get(id=1)
    # 判断是否有效
    serializer.is_valid()
    # 如果无效不给更新
    serializer.update(obj, serializer.validated_data)




if __name__ =="__main__":
    obj = Post.objects.get(id=1)
    serializer = PostSerializer(instance=obj)
    print(serializer.data)
    print(Post.objects.filter(id=1).values()[0])




