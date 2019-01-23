from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView, UpdateView, DeleteView
from django_tables2 import SingleTableView, SingleTableMixin

from abercompsoc.voting.models import Election, UserElectionOption
from abercompsoc.voting.tables import ElectionTable, UserElectionOptionTable


class ElectionList(SingleTableView):
    model = Election
    table_class = ElectionTable
    template_name = "voting/elections_list.html"

    def get_table_kwargs(self):
        kwargs = super(ElectionList, self).get_table_kwargs()
        kwargs.update({"user": self.request.user})
        return kwargs


class UserElectionDetails(SingleTableMixin, DetailView):
    model = Election
    table_class = UserElectionOptionTable
    template_name = "voting/election_details.html"
    pk_url_kwarg = "election_id"

    def get_table_data(self):
        return self.get_object().userelectionoption_set.all()


class UserElectionOptionUpdate(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = UserElectionOption
    template_name = "voting/option_details.html"
    fields = ["manifesto"]
    success_message = "Your manifesto has been updated!"

    def get_object(self, queryset=None):
        instance, _ = self.model.objects.get_or_create(runner=self.request.user, election_id=self.kwargs.get("election_id"))
        return instance

    def get_success_url(self):
        return self.get_object().get_absolute_url()


class UserElectionOptionDelete(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = UserElectionOption
    template_name = "voting/option_confirm_delete.html"
    success_message = "You are no longer running in this election"

    def get_object(self, queryset=None):
        return get_object_or_404(self.model, runner=self.request.user, election_id=self.kwargs.get("election_id"))

    def get_success_url(self):
        return reverse("voting:election_details", kwargs={"election_id":self.kwargs.get("election_id")})


class UserElectionOptionVote(LoginRequiredMixin, View):

    def post(self, *args, **kwargs):
        election_id = self.kwargs.get("election_id")
        option = get_object_or_404(UserElectionOption, id=self.kwargs.get("option_id"), election__id=election_id)
        election = get_object_or_404(Election, id=election_id)
        
        # Check if the user has voted in this election
        if election.can_vote(self.request.user):
            self.vote_for_election_option(election, option)
        else:
            if self.request.user.election_set.filter(id=election_id).exists():
                messages.add_message(self.request, messages.ERROR, 'You have already voted in this election.')
            elif not election.is_open():
                messages.add_message(self.request, messages.ERROR, 'The selected election is currently not open ')
            elif not self.request.user.is_aber_student() and election.aber_only:
                messages.add_message(self.request, messages.ERROR, 'This election requires you to have a verified '
                                                                   '@aber.ac.uk email address')
            else:  # If we reach this point, then you should look for any extra variables added in election.can_vote
                messages.add_message(self.request, messages.ERROR, 'Something Happened!')
                from sentry_sdk import capture_message
                capture_message("A user could not vote, but we couldn't work out why", level="Error")
        return redirect(election.get_absolute_url())

    def vote_for_election_option(self, election, option):
        """
        Vote for Allows a user to vote for an election option, without checking if its valid beforehand
        :param election: The election to vote in
        :param option: The option to vote for
        """
        election.voters.add(self.request.user)
        option.votes = option.votes + 1
        messages.add_message(self.request, messages.SUCCESS, 'Your vote has been placed.')
        option.save()
        election.save()


