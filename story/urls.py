from django.urls import path
from . import views

app_name = 'story'

urlpatterns = [
 	path('story/', views.story_list, name='story_list'),
   	path('detail/<str:slug>/', views.story_detail, name='story_detail'),
]