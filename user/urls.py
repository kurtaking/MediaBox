from django.conf.urls import url, include
from . import views

urlpatterns = [
  url(r'^$', views.Index.as_view(), name='index'),
  url(r'^users/$', views.UserList.as_view(), name='users'),
  url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user_detail'),
]
