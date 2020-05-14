from django import forms
from .models import Comment

class ContactForm(forms.Form):
	name = forms.CharField(required = True, widget=forms.TextInput(attrs={
		'class':'control'
		}))
	email = forms.EmailField(required = True, widget=forms.EmailInput(attrs={
		'class':'control'
		}))
	message = forms.CharField(required = True,
							widget=forms.Textarea(attrs={
								'class':'control'
								})
							)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')
        widgets={
        	'name':forms.TextInput(attrs = {'class':'control'}),
        	'body':forms.Textarea(attrs={'class': 'control'})
        }