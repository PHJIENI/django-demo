from django.conf.urls import url
from django.urls import path,include,re_path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views
urlpatterns = [
    path("post_list/getlist", views.post_list),
    # 通过url传递参数
    re_path("post_list/getlist/(?P<pk>[0-9]*)", views.getParamsFromUrl),
    path("post_list/apiview", views.api_view_post_list),
    url(r'post_list/posts/$', views.PostList.as_view(), name='posts'),
]
urlpatterns = format_suffix_patterns(urlpatterns)