from django.db import models
# python manage.py makemigrations #为改动创建迁移记录；
# python manage.py migrate  #将操作同步到数据库。
# Create your models here.
from django.utils.html import strip_tags


class Post(models.Model):
    title = models.CharField(max_length=70)
    body = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    excerpt = models.CharField(max_length=200,blank=True)

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        if not self.excerpt:
            self.excerpt = strip_tags(self.body)[:50]
        super(Post,self).save(*args, **kwargs)
