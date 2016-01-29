from rest_framework import viewsets

from .models import HelpRequest
from core.serializers import HelpRequestSerializer


class HelpRequestViewSet(viewsets.ModelViewSet):
    serializer_class = HelpRequestSerializer

    def get_queryset(self):
        skills = self.request.query_params.get('skills', None)
        _type = self.request.query_params.get('type', None)
        if skills:
            print skills.split(',')
        if _type:
            print _type.split(',')
        return HelpRequest.objects.all()
