from __future__ import unicode_literals
from model_utils.models import TimeStampedModel

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from taggit.managers import TaggableManager


class UserProfile(TimeStampedModel):
    FELLOWS = u'F'
    CTO = u'B'
    INTERNSHIP = u'I'
    EXPERIENCE = u'E'
    PROGRAM_CHOICES = (
        (FELLOWS, 'Fellows'),
        (CTO, 'CTO Bootcamp'),
        (INTERNSHIP, 'Internship'),
        (EXPERIENCE, 'Experience'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nationality = models.CharField(max_length=255)
    current_location = models.CharField(max_length=255)
    work = models.CharField(max_length=255)
    startup_status = models.BooleanField(default=False)
    portfolio_status = models.BooleanField(default=False)
    itc_program_name = models.CharField(max_length=1,
                                        choices=PROGRAM_CHOICES,
                                        default=EXPERIENCE)
    itc_program_year = models.IntegerField(default=2010, validators=[MinValueValidator(2013),
                                                                     MaxValueValidator(2016)])
    linked_in_url = models.CharField(max_length=255)
    skills = TaggableManager()

    class Meta:
        verbose_name_plural = 'User Profiles'
        verbose_name = 'User Profile'

    def __unicode__(self):
        return u'%s: Profile' % self.user.email
