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

def create(**kwargs):
    """
    增
    """
    Post.objects.create(id = kwargs.get("id", None))


def delete(**kwargs):
    """
    删
    """
    Post.objects.get(id = "").delete()

def update():
    """
    改
    """
    Post.objects.filter(id="").update(title = "")

def select():
    """
    查
    """
    Post.objects.filter(id="").values()

def selectAll():
    """
    查询全部
    """
    Post.objects.all().values()


if __name__ == "__main__":
    Post.objects.create(title="test_DB", body="start_practise",excerpt="start")
    # res = Post.objects.all().values()
    # res = Post.objects.get(id = "2")
    # res.body = "update1"
    # res.save()
    # Post.objects.get(id = 3).delete()
    # print(res.create_time)
    pass



