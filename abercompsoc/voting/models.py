import datetime
import pytz

from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import DateTimeRangeField
from django.contrib.postgres.forms import RangeWidget
from django.db import models

# Create your models here.
from django.urls import reverse
from markdownx.models import MarkdownxField

User = get_user_model()


class Election(models.Model):
    """
    An election, which keeps track of the options to vote for, and who has voted within it.
    """
    title = models.CharField(max_length=255, default="")
    description = MarkdownxField(default="")
    created = models.DateTimeField(auto_now_add=True)
    voters = models.ManyToManyField(User, blank=True)
    open_time = DateTimeRangeField()

    def get_absolute_url(self):
        return reverse("voting:election_details", kwargs={"election_id": self.id})

    def __str__(self):
        return self.title

    def is_open(self):
        return pytz.utc.localize(datetime.datetime.now()) in self.open_time

    def can_vote(self, user):
        """
        Check that the election is currently open and that the user has not already voted
        :param user: The user to check has voted
        :return: True if the user can vote
        """
        return self.is_open() and user not in self.voters


class ElectionOption(models.Model):
    """
    A voting option for an Election
    """
    votes = models.IntegerField(default=0)
    election = models.ForeignKey(Election, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class UserElectionOption(ElectionOption):
    """
    Used when a user can run for an election
    """
    runner = models.ForeignKey(User, on_delete=models.CASCADE)
    manifesto = MarkdownxField(default="")

    def get_absolute_url(self):
        return reverse("voting:election_option_update", kwargs={"election_id": self.election_id})
