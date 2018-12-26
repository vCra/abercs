from django.contrib import admin

# Register your models here.
from django.contrib.admin.widgets import AdminDateWidget, AdminSplitDateTime
from django.contrib.postgres.fields import DateTimeRangeField
from django.contrib.postgres.forms import RangeWidget
from django.forms import DateTimeField

from abercompsoc.voting.models import Election, UserElectionOption



class ElectionAdmin(admin.ModelAdmin):
    pass


admin.site.register(Election, ElectionAdmin)

admin.site.register(UserElectionOption)
