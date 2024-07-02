from django.contrib import admin
from .models import Post, Comment

# Register your models here.
# admin.site.register(Post)
# admin.site.register(Comment)


# admin 사이트에서 보여주는 방식
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
    list_display_links = ["created_at"]  # 맨 처음 보여주는거 기본값
    search_fields = ["title"]


class CommentAdmin(admin.ModelAdmin):
    list_display = ("user", "created_at")


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
