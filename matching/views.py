from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import HelpRequest


@method_decorator(login_required)
class HelpRequestMatchView(ListView):
    model = HelpRequest

    def get_queryset(self):
        return HelpRequest.objects.filter(provider=None)
