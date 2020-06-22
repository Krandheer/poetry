from django.shortcuts import render
from .forms import NewsUserForm
from . models import NewsUsers
from django.core.mail import send_mail


def newsletter_subscribe(request):
	template = "newsletter/subscribe.html"
	return render(request, template, context={})

# def newsletter_subscribe(request):
# 	if request.method == 'POST':
# 		form = NewsUserForm(request.POST)
# 		if form.is_valid():
# 			instance = form.save(commit=False)
# 			if NewsUsers.objects.filter(email=instance.email).exists():
# 				print("you have subscribed already")
# 			else:
# 				instance.save()
# 				form = NewsUserForm()
# 			print('your email is added to our database')
# 			# send_mail('Bhashadiaries blog ', 'welcome', 
# 			# 			'bhaskarpandey003@gmail.com', [instance.email], fail_silently=False)
# 	else:
# 		form = NewsUserForm()
# 	context = {'form':form}
# 	template = "newsletter/subscribe.html"
	
# 	return render(request, template, context)

#I need to write a function which will pull my new content and sent it
#to my subscriber as newsletter, email service provider will give me
#the list of my subscriber to whom I will be sending new content


#when this is complete I have to add a alert message in template, so that when
#somebody subscribes he gets a mail for confirmation as well as instant 
#popup message which will say you have subscribed successfully please
#check your email for verification of subscription.