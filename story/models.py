from django.db import models
from django.contrib.auth.models import User

STATUS=(
	(0, "Draft"),
	(1,"Publish")
	)

class Story(models.Model):
	title=models.CharField(max_length=200, unique=True)
	slug = models.SlugField(max_length=200,unique=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='story')
	image = models.ImageField(upload_to='images/', blank=True)
	updated_on =models.DateTimeField(auto_now=True)
	content = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)
	status = models.IntegerField(choices=STATUS, default=0)


	class Meta:
		ordering=['-created_on']
		verbose_name ='story'
		verbose_name_plural ='stories'

	def __str__(self):
		return self.title


class Comment(models.Model):
    name = models.CharField(max_length=200)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    # approved_comment = models.BooleanField(default=False)
    post = models.ForeignKey(Story,on_delete=models.CASCADE, related_name='comments')

    class Meta:
        ordering = ['created_on']

    # def approve(self):
    #     self.approved_comment = True
    #     self.save()

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
