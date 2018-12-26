import django_tables2 as tables

from .models import Election, UserElectionOption


class ElectionTable(tables.Table):

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user")
        super().__init__(*args, **kwargs)


    class Meta:
        model = Election
        fields = [
            'title',
            'start',
        ]

    title = tables.columns.LinkColumn()
    start = tables.columns.DateTimeColumn(verbose_name="Opening Date", accessor="open_time.lower")
    end = tables.columns.DateTimeColumn(verbose_name="Closing Date", accessor="open_time.upper")
    voted = tables.columns.BooleanColumn()

    def value_voted(self, record):
        return not record.voters.filter(pk=self.user.pk).exists()


class UserElectionOptionTable(tables.Table):
    class Meta:
        model = UserElectionOption

        fields = [
            'runner',
            'manifesto',
            'vote',
        ]

    runner = tables.columns.RelatedLinkColumn()
    manifesto = tables.columns.TemplateColumn(template_name="voting/tables/user_election_option_manifesto_button.html")
    vote = tables.columns.TemplateColumn(template_name="voting/tables/user_election_option_vote_button.html")
