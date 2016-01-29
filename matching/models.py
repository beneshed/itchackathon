from __future__ import unicode_literals

from model_utils.models import TimeStampedModel
from django.contrib.auth.models import User
from django.db import models
from taggit.managers import TaggableManager


class HelpRequest(TimeStampedModel):
    SKYPE = 'S'
    FACE2FACE = 'F'
    INDIFFERENT = 'I'
    LOCATION_CHOICES = (
        (SKYPE, 'Skype'),
        (FACE2FACE, 'Face To Face'),
        (INDIFFERENT, 'Indifferent'),
    )
    MENTORING = 'M'
    INTERVIEW_PREP = 'P'
    TYPE_CHOICES = (
        (MENTORING, 'Mentoring'),
        (INTERVIEW_PREP, 'Interview Prep'),
    )
    TECHNICAL = 'T'
    HR = 'H'
    INTERVIEW_PREP_CHOICES = (
        (TECHNICAL, 'Technical'),
        (HR, 'HR'),
    )
    BUSINESS = 'B'
    MENTORING_CHOICES = (
        (TECHNICAL, 'Technical'),
        (BUSINESS, 'Business'),
    )
    requester = models.ForeignKey(User, related_name='req')
    provider = models.ForeignKey(User, related_name='pro', null=True, blank=True)
    type = models.CharField(max_length=1, choices=TYPE_CHOICES,
                            default=INTERVIEW_PREP)
    interview_prep_choices = models.CharField(max_length=1, choices=INTERVIEW_PREP_CHOICES,
                                              null=True, blank=True)
    mentoring_choices = models.CharField(max_length=1, choices=MENTORING_CHOICES,
                                         null=True, blank=True)
    urgent = models.BooleanField(default=False)
    location = models.CharField(max_length=1, choices=LOCATION_CHOICES,
                                default=FACE2FACE)
    date_start = models.DateField()
    date_end = models.DateField()
    tags = TaggableManager(blank=True)

    class Meta:
        verbose_name = u'Help Request'
        verbose_name_plural = u'Help Requests'

    def __unicode__(self):
        return u'%s\'s help request' % self.requester.get_full_name()

