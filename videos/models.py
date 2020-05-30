from django.db import models
from django.contrib.auth.models import User

STATUS=(
	(0, "Draft"),
	(1,"Publish")
	)

class Video(models.Model):
	title=models.CharField(max_length=200, unique=True)
	slug = models.SlugField(max_length=200,unique=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='video')
	video = models.FileField(upload_to='videos/', blank=True)
	video_description = models.TextField()
	updated_on =models.DateTimeField(auto_now=True)
	created_on = models.DateTimeField(auto_now_add=True)
	status = models.IntegerField(choices=STATUS, default=0)


	class Meta:
		ordering=['-created_on']
		verbose_name ='video'
		verbose_name_plural ='videos'

	def __str__(self):
		return self.title