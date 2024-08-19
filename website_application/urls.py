from django.urls import path
from . import views
from .views import get_home_view, get_post_view, open_resume, get_login_view, get_logout_view


urlpatterns = [
	path("", get_home_view, name="index"),
	path("post/<int:pk>", get_post_view, name="post"),
	path("resume", open_resume, name="resume"),
	path("login", get_login_view, name="login"),
	path("logout", get_logout_view, name="logout")
]
