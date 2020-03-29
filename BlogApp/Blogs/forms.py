from django import forms
from .models import BlogUser
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class BlogForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'content')

class NewPostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'content', 'genre')


class RegForm(UserCreationForm):
	email = forms.EmailField()
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'password1', 'password2', 'email')


class searchPost(forms.ModelForm):
	class Meta:
		model = Post
		fields = {'genre'}
	# def get():
	# 	return self.genre