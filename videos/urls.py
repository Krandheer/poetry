from django.urls import path
from . import views

app_name = 'videos'

urlpatterns = [
	path('videos/', views.video_list, name='video_list'),
   	path('detail/<str:slug>/', views.video_detail, name='video_detail'),
]