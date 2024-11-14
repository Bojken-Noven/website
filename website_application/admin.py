from django.contrib import admin
from .models import Post, Resume, RightSideBarContent, Video
from django_summernote.admin import SummernoteModelAdmin


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ("body")

class RightSideBarContentAdmin(SummernoteModelAdmin):
    summernote_fields = ("body")

admin.site.register(Post, PostAdmin)
admin.site.register(Resume)
admin.site.register(RightSideBarContent, RightSideBarContentAdmin)
admin.site.register(Video)
