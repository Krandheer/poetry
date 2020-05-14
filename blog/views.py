from django.shortcuts import render, redirect, get_object_or_404
from . models import Post, Comment
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from .forms import ContactForm, CommentForm
from django.db.models import Q



def home(request):
	posts = Post.objects.filter(status=1).order_by('-created_on')[:3]
	return render(request=request,
				template_name='blog/home.html',
				context= {'posts': posts})
	#I can get the model of story and thought here
	#and iterate throught them on home.html to show
	#them in home page.

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
	form = ContactForm(request.POST or None)
	context = { "form": form}
	if form.is_valid():
		print(form.cleaned_data)
		form=ContactForm()
	return render(request, "blog/contact_page.html", context)












