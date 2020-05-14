from django.shortcuts import render
from .forms import NewsUserForm
from . models import NewsUsers
from django.core.mail import send_mail

def newsletter_subscribe(request):
	if request.method == 'POST':
		form = NewsUserForm(request.POST)
		if form.is_valid():
			instance = form.save(commit=False)
			if NewsUsers.objects.filter(email=instance.email).exists():
				print("you have subscribed already")
			else:
				instance.save()
			print('your email is added to our database')
			send_mail('Bhashadiaries blog ', 'welcome', 
						'bhaskarpandey003@gmail.com', [instance.email], fail_silently=False)
	else:
		form = NewsUserForm()
	context = {'form':form}
	template = "newsletter/subscribe.html"
	return render(request, template, context)