from django.contrib import admin
from .models import Post


class PostModelAdmin(admin.ModelAdmin):

    list_display = ["id","title", "content", "updated", "created"]
    list_display_links = ["title"]
    list_display_filter = ["updated", "created"]
    search_fields = ["title", "content"]
    class Meta:
        model = Post

admin.site.register(Post, PostModelAdmin)
