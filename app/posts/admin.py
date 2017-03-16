from django.contrib import admin
from .models import Post, Comment
from mediumeditor.admin import MediumEditorAdmin

class PostModelAdmin(MediumEditorAdmin, admin.ModelAdmin):

    list_display = ["id","title", "content", "updated", "created"]
    list_display_links = ["title"]
    list_display_filter = ["-updated", "-created"]
    search_fields = ["title", "content"]
    mediumeditor_fields = ('content') 
    class Meta:
        model = Post

class CommentModelAdmin(admin.ModelAdmin):

	list_display = ["id", "user", "content", "updated", "created"]
	list_display_links = ["user"]
	search_fields = ["content"]

	class Meta:
		model = Comment

admin.site.register(Post, PostModelAdmin)
# admin.site.register(Comment, CommentModelAdmin)