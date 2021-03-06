from django.urls import path, re_path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('note', views.note_list, name='note_list'),

    path('post', views.post_list, name='post_list'),

    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),




]

