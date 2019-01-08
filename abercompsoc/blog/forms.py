from django import forms
from markdownx.fields import MarkdownxFormField

from abercompsoc.blog.models import Comment


class UserCommentForm(forms.ModelForm):

    bodytext = MarkdownxFormField()

    class Meta:
        model = Comment
        fields = ["bodytext"]

