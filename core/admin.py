from django.contrib import admin

from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'nationality',
                    'current_location', 'work', 'startup_status',
                    'portfolio_status', 'itc', 'linked_in')

    def itc(self, obj):
        return '%s:%d' % (obj.itc_program_name, obj.itc_program_year)

    def linked_in(self, obj):
        return '<a href="%s">%s</a>' % (obj.linked_in_url, obj.linked_in_url)
