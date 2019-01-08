from django_tables2 import tables


class BlogTable(tables.Table):
    title = tables.columns.LinkColumn()
    post_date = tables.columns.DateTimeColumn(verbose_name='Posted')
    posted_by = tables.columns.RelatedLinkColumn()
