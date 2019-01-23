from django_tables2 import tables


class EventTable(tables.Table):
    event_name = tables.columns.LinkColumn()
    start = tables.columns.DateTimeColumn(verbose_name='Starts', accessor="date.lower")
    end = tables.columns.DateTimeColumn(verbose_name="Ends", accessor="date.upper")
