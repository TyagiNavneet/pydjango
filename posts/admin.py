from django.contrib import admin

# Register your models here.
from posts.models import Post

class PostModelAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'title','updated','timestamp']
    list_display_links = ['updated']
    list_filter = ['title','updated']
    class Meta:
        model = Post
        
    

admin.site.register(Post, PostModelAdmin)
