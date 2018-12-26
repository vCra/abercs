from django.urls import path

from abercompsoc.voting.views import ElectionList, UserElectionDetails, UserElectionOptionVote, \
    UserElectionOptionUpdate, UserElectionOptionDelete

app_name = "abercompsoc.voting"

urlpatterns = [
    path("", view=ElectionList.as_view(), name="election_lst"),
    path("<int:election_id>/", view=UserElectionDetails.as_view(), name="election_details"),
    path("<int:election_id>/<int:option_id>/vote/", view=UserElectionOptionVote.as_view(), name="election_option_vote"),
    path("<int:election_id>/run/", view=UserElectionOptionUpdate.as_view(), name="election_option_update"),
    path("<int:election_id>/run/delete", view=UserElectionOptionDelete.as_view(), name="election_option_delete"),
]
