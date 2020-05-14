from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.post_list, name='post_list'),
    path('blog/<str:slug>/', views.post_detail, name='post_detail'),
    path('contact/', views.contact_page, name = 'contact_page'),
    # path('post/<str:slug>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
]