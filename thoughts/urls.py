from django.urls import path
from . import views

app_name = 'thoughts'

urlpatterns = [
 	path('thoughts/', views.thoughts_list, name='thoughts_list'),
   	path('detail/<str:slug>/', views.thoughts_detail, name='thoughts_detail'),
]