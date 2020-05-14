from tinymce.widgets import TinyMCE
from django.db import models
from django.contrib import admin
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
	list_display=('title', 'slug', 'status', 'created_on')
	list_filter=('status','title')
	search_fields=['title', 'content']
	prepopulated_fields = {'slug':('title',)}

	formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }

admin.site.register(Post, PostAdmin)


admin.site.register(Comment)
admin.site.site_header="bhashadiaries"

