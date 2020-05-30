from tinymce.widgets import TinyMCE
from django.db import models
from django.contrib import admin
from .models import Video

class VideoAdmin(admin.ModelAdmin):
	list_display=('title', 'slug', 'status', 'created_on')
	list_filter=('status','title')
	search_fields=['title', 'video_description']
	prepopulated_fields = {'slug':('title',)}

	formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }

admin.site.register(Video, VideoAdmin)