from rest_framework import viewsets
from taggit.models import Tag, TaggedItem

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
