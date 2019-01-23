from django.contrib import admin

# Register your models here.
from abercompsoc.blog.models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'post_date', 'posted_by',
                    'allow_comments')


class CommentAdmin(admin.ModelAdmin):

    list_display = ('user', 'post_date')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
