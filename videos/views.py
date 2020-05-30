from django.shortcuts import render
from . models import Video

def video_list(request):
	posts = Video.objects.filter(status=1).order_by('-created_on')
	return render(request,'videos/video_list.html',{'posts':posts})


def video_detail(request,slug):
	posts = Video.objects.get(slug=slug)
	return render(request, 'videos/video_detail.html',{'posts':posts})
