from rest_framework import serializers
from django.contrib.auth.models import User
from taggit.models import Tag, TaggedItem

from .models import UserProfile
from matching.models import HelpRequest


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email')


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserProfile


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag


class TaggedItemSerializer(serializers.ModelSerializer):
    tag = TagSerializer()

    class Meta:
        model = TaggedItem


class HelpRequestSerializer(serializers.ModelSerializer):
    requester = UserSerializer()
    provider = UserSerializer()

    class Meta:
        model = HelpRequest
