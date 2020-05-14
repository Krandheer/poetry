from django.shortcuts import render
from .models import Story, Comment
from .forms import CommentForm

def story_list(request):
	posts = Story.objects.filter(status=1).order_by('-created_on')
	return render(request,'story/story_list.html',{'posts':posts})

def story_detail(request,slug):
	posts = Story.objects.get(slug=slug)

	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			comment=Comment(
				name=form.cleaned_data['name'],
				body=form.cleaned_data['body'],
				post=posts)
			comment.save()
	else:
		form=CommentForm()

	comments = Comment.objects.filter(post=posts)
	context={
		'posts':posts,
		'comments':comments,
		'form':form,
	}
	return render(request, 'story/story_detail.html',context)


