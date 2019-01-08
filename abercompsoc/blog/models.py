from django.conf import settings
from django.db import models
from django.urls import reverse
from markdownx.models import MarkdownxField


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title")
    slug = models.SlugField()
    body = MarkdownxField()
    post_date = models.DateTimeField(auto_now_add=True, verbose_name="Post Date")
    modified = models.DateTimeField(null=True, verbose_name="Modified")
    posted_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, verbose_name="Posted by", on_delete=models.SET_NULL)
    allow_comments = models.BooleanField(default=True, verbose_name="Allow Comments")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        kwargs = {
            'slug': self.slug,
            'year': '%04d' % self.post_date.year,
            'month': '%02d' % self.post_date.month,
            'day': '%02d' % self.post_date.day,
        }

        return reverse('blog:blog_detail', kwargs=kwargs)


class Comment(models.Model):
    post = models.ForeignKey(
        Post, related_name='comments', verbose_name="Post",
        on_delete=models.CASCADE)

    bodytext = models.TextField(verbose_name="Message")

    post_date = models.DateTimeField(
        auto_now_add=True, verbose_name="Post date")

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="User", related_name='comment_user',
        on_delete=models.CASCADE)

    def __str__(self):
        return self.bodytext
