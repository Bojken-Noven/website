from django.shortcuts import render


def index(request):
	return render(request, "index.html")

def tech(request):
	return render(request, "tech.html")

def music(request):
	return render(request, "music.html")

def misc(request):
	return render(request, "misc.html")
