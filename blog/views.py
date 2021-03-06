from django.shortcuts import render, redirect, get_object_or_404
from . models import Post, Comment
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from .forms import CommentForm
from django.db.models import Q
from story.models import Story
from thoughts.models import Thoughts

def home(request):
	total_poems = Post.objects.all().count()
	total_story = Story.objects.all().count()
	total_thoughts = Thoughts.objects.all().count()
	posts = Post.objects.filter(status=1).order_by('-created_on')[:3]
	story = Story.objects.filter(status=1).order_by('-created_on')[:3]
	thoughts = Thoughts.objects.filter(status=1).order_by('-created_on')[:3]
	return render(request=request,
				template_name='blog/home.html',
				context= {'posts': posts,
							'stories': story,
							'thoughts': thoughts,
							'total_poems':total_poems,
							'total_story':total_story,
							'total_thoughts':total_thoughts})
	#I can use model from different aap here
	#and use them in home.html template
	#to show the home page list from different model

def post_list(request):
	posts = Post.objects.filter(status=1).order_by('-created_on')
	return render(request, 'blog/post_list.html',{'posts': posts})

def post_detail(request, slug):
	posts = Post.objects.get(slug=slug)

	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = Comment(
				name = form.cleaned_data["name"],
				body = form.cleaned_data["body"],
				post = posts
				)
			comment.save()
			form = CommentForm()
	else:
		form = CommentForm() 

	comments = Comment.objects.filter(post=posts)
	context = {
				'posts': posts,
				'comments':comments,
				'form': form,
				}

	return render(request, 'blog/post_detail.html', context)

#backend for receiving detail is yet to be set
def contact_page(request):
	context = {}
	return render(request, "blog/contact_page.html", context)












