from django.shortcuts import render, redirect
from .models import Video, Post, RightSideBarContent, Resume
from django.http import FileResponse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout


def get_home_view(request):
	videos = Video.objects.all()
	posts = Post.objects.all()
	right_side_bar_content = RightSideBarContent.objects.latest("date")
	context = {
		"videos": videos,
		"posts": posts, 
		"right_side_bar_content": right_side_bar_content
	}
	return render(request, "index.html", context)

def get_post_view(request, pk):
	post = Post.objects.get(pk=pk)
	context = {
		"post": post
	}
	return render(request, "post.html", context)

def open_resume(request):
	file_path = "/" + Resume.objects.latest("date").pdf.name
	return FileResponse(open(settings.MEDIA_ROOT + file_path, "rb"))

def get_login_view(request):
	error = ""
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(request, username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect("admin:index")
			else:
				error = "Incorrect login credentials."
				form = LoginForm()
	else:
		form = LoginForm()

	context = {
		"form": form,
		"error": error
	}

	return render(request, "login.html", context)

def get_logout_view(request):
	logout(request)
	return redirect("index")
