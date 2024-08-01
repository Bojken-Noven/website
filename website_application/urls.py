from django.urls import path
from . import views


urlpatterns = [
	path("", views.index, name="index"),
	path("tech/", views.tech, name="tech"),
	path("music/", views.music, name="music"),
	path("misc/", views.misc, name="misc"),
]
