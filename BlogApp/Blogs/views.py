from django.shortcuts import render, get_object_or_404, redirect
from .forms import BlogForm, NewPostForm, RegForm, searchPost
from .models import Post, BlogUser
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def loginpage(request):
	if request.method == 'POST':
		form = searchPost(request.POST)
		genre = request.POST.get('genre')
		return redirect('viewpost', genre = genre)
	else: 
		form = searchPost()
	return render(request, 'Blogs/loginpage.html', {'form' : form})


def viewposts(request, genre):
	posts = Post.objects.filter(genre = genre)
	return render(request, 'Blogs/viewp.html', {'posts' : posts})

@login_required
def dashboard(request, user_name):
	name = BlogUser.objects.get(user__username = user_name)
	post = Post.objects.filter(Publisher = name)
	return render(request, 'Blogs/dashboard.html', {'post' : post})

@login_required
def postedit(request, pk):
	post = get_object_or_404(Post, pk = pk)
	author = post.Publisher
	person = author.user
	name = person.username
	if request.method == "POST":
		form = BlogForm(request.POST or None, instance = post)
		if form.is_valid():
			form.save()
			post.save()
			return redirect('dashboard', user_name = name)
	else :
		form = BlogForm(instance = post)
		return render(request, 'Blogs/editpost.html', {'form' : form})


@login_required
def user_logout(request):
	logout(request)
	return redirect('loginpage')


@login_required
def addpost(request):
	if request.method == "POST":
		form = NewPostForm(request.POST)
		if form.is_valid():
			post = form.save(commit = False)
			person = request.user
			Publishquery = BlogUser.objects.filter(user = person)
			for x in Publishquery:
				post.Publisher = x
			post.save()
			return redirect('dashboard', user_name = person.username)
		else:
			form = NewPostForm()
	else:
		form = NewPostForm()
		return render(request, 'Blogs/new_post.html', {'form' : form})

def register(request):
	if request.method == 'POST':
		form = RegForm(request.POST)
		if form.is_valid():
			person = form.save()
			person.save()
			B = BlogUser(user = person)
			B.save()
			return redirect('user_login')
	else:	
		form = RegForm()
	return render(request, 'Blogs/registration.html', {'form' : form})



def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		person = authenticate(username = username, password = password)
		if person is not None:
			print("hola")
			login(request, person)
						
			return redirect('dashboard', user_name = person.username)
		else:
				return HttpResponse("Invalid Login Credentials")
	else:
		return render (request, 'Blogs/login.html', {})




