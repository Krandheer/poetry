from django.shortcuts import render
from .models import Thoughts,Comment
from .forms import CommentForm

def thoughts_list(request):
	posts = Thoughts.objects.filter(status=1).order_by('-created_on')
	return render(request,'thoughts/thoughts_list.html', {'posts':posts})

def thoughts_detail(request, slug):
	posts = Thoughts.objects.get(slug=slug)

	if request.method=='POST':
		form=CommentForm(request.POST)
		if form.is_valid():
			comment=Comment(
				name=form.cleaned_data['name'],
				body=form.cleaned_data['body'],
				post=posts)
			comment.save()
	else:
		form=CommentForm()

	comments=Comment.objects.filter(post=posts)
	context={
		'posts':posts,
		'comments':comments,
		'form':form,
	}
	return render(request,'thoughts/thoughts_detail.html', context)


