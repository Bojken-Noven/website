from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from website_application.views import get_home_view
from django.shortcuts import redirect


urlpatterns = [
    path('', include('website_application.urls')),
    path('admin/login/', lambda request: redirect('index')),
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
