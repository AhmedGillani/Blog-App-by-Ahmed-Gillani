from django.contrib import admin
from .models import Post, Feed

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'image', 'content', 'date', 'author']


@admin.register(Feed)
class FeedAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'phone', 'email', 'feed', 'date']
