from django.contrib import admin
from django.conf import settings 
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('story/', include('story.urls')),
    path('thoughts', include('thoughts.urls')),
    path('newsletter/', include('newsletter.urls')),
    path('tinymce/', include('tinymce.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)