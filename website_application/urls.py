from django.urls import path
from . import views
from .views import get_home_view, get_post_view, open_resume


urlpatterns = [
	path("", get_home_view, name="index"),
	path("post/<int:pk>", get_post_view, name="post"),
	path("resume", open_resume, name="resume")
]
