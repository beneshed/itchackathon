from rest_framework import viewsets
from rest_framework.views import APIView
from taggit.models import Tag, TaggedItem
from rest_framework.response import Response

from .serializers import UserProfileSerializer, TagSerializer, TaggedItemSerializer
from .models import UserProfile


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class TagViewReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TaggedItemReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TaggedItem.objects.all()
    serializer_class = TaggedItemSerializer


class SuggestView(APIView):
    authentication_classes = ()
    permission_classes = ()

    def get(self, request, format=None):
        cluster = UserProfile.objects.get(user__email=self.request.query_params.get('email', None)).cluster
        suggestions = UserProfile.objects.filter(cluster=cluster).exclude(
            user__email=self.request.query_params.get('email', None))
        response = UserProfileSerializer(suggestions, many=True)
        return Response(response.data)
