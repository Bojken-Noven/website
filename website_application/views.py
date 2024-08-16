from django.shortcuts import render
from .models import Video, Post, RightSideBarContent, Resume
from django.http import FileResponse
from django.conf import settings


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
