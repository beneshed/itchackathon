from django.contrib import admin

from .models import HelpRequest


@admin.register(HelpRequest)
class HelpRequestAdmin(admin.ModelAdmin):
    list_display = ('requester', 'provider', 'type',
                    'interview_prep_choices', 'mentoring_choices',
                    'urgent', 'date_start', 'date_end', 'location')
    list_filter = ('urgent', 'location')
