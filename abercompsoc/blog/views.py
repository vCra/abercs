from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import DetailView, DateDetailView
from django_tables2 import SingleTableView

from abercompsoc.blog.forms import UserCommentForm
from abercompsoc.blog.models import Post, Comment
from abercompsoc.blog.tables import BlogTable


class BlogDetailView(DateDetailView):
    model = Post
    date_field = 'post_date'
    month_format = '%m'

    def get_queryset(self):
        queryset = super(BlogDetailView, self).get_queryset()
        return queryset.select_related()

    def post(self, request, *args, **kwargs):
        self.object = post = self.get_object()
        if request.user.is_authenticated:
            form = UserCommentForm(request.POST)
        else:
            return HttpResponseForbidden()
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect(post.get_absolute_url())
        context = self.get_context_data(object=post)
        context['comment_form'] = form
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        form = UserCommentForm()

        context = {
            'comment_form': form,
            'comments': Comment.objects.filter(post=self.object.id).select_related()
        }
        return super(BlogDetailView, self).get_context_data(**context)


class BlogTableView(SingleTableView):
    table_class = BlogTable
    model = Post
