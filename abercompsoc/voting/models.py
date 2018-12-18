from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import DateTimeRangeField
from django.db import models

# Create your models here.

User = get_user_model()


class Election(models.Model):
    """
    An election, which keeps track of the options to vote for, and who has voted within it.
    """
    created = models.DateTimeField(auto_now_add=True)
    voters = models.ManyToManyField(User)
    open_time = DateTimeRangeField()


class ElectionOption(models.Model):
    """
    A voting option for an Election
    """
    votes = models.IntegerField()

    class Meta:
        abstract = True


class UserElectionOption(ElectionOption):
    """
    Used when a user can run for an election
    """
    runner = models.ForeignKey(User, on_delete=models.CASCADE())
