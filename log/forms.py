from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

from blog.models import BlogPost
from home.models import Info, Team
from event.models import Events


class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta():
		model = User
		fields = ['username', 'email','password']


class UserProfileForm(forms.ModelForm):

	class Meta():
		model = UserProfile
		fields = ['club']

class BlogAddForm(forms.ModelForm):

	class Meta:
		model = BlogPost
		fields = ['title','image' , 'content']
		widgets = { 'title': forms.TextInput(attrs={'placeholder': 'Title', 'class': 'form-control'}),
					'content': forms.Textarea(attrs={'placeholder': 'Write your post...', 'class': 'form-control' }),

		}


class InfoAddForm(forms.ModelForm):

	class Meta:
		model = Info
		fields = ['title', 'content']
		widgets = { 'title': forms.TextInput(attrs={'placeholder': 'type "information"'}),
				'content': forms.Textarea(attrs={'placeholder': 'Describe your club...'}),

		}


class TeamAddForm(forms.ModelForm):

	class Meta:
		model = Team
		fields = ['name', 'image', 'designation', 'facebook', 'github', 'linkedin']
		widgets = { 'name': forms.TextInput(attrs={'placeholder': 'Name'}),
					'designation': forms.TextInput(attrs={'placeholder': 'Designation'}),
					'facebook': forms.TextInput(attrs={'placeholder': 'facebook'}),
					'github': forms.TextInput(attrs={'placeholder': 'github'}),
					'linkedin': forms.TextInput(attrs={'placeholder': 'linkedin'}),




		}


class EventAddForm(forms.ModelForm):

	class Meta:
		model = Events
		fields = ['title', 'date', 'time', 'venue', 'content']
		widgets = { 'title': forms.TextInput(attrs={'placeholder':'Title', 'class': 'form-title'}),
				'venue': forms.TextInput(attrs={'placeholder': 'Venue', 'class': 'form-control'}),
				'content': forms.Textarea(attrs={'placeholder': 'Enter the details about the event...'})


		}




