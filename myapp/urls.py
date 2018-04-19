from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post', views.post_list, name='post_list'),
    path('note', views.note_list, name='note_list'),
]

