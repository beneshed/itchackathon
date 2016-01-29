from __future__ import unicode_literals
import calendar

from model_utils.models import TimeStampedModel
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from taggit.managers import TaggableManager
from django.conf import settings

class UserProfile(TimeStampedModel):
    FELLOWS = u'F'
    CTO = u'B'
    INTERNSHIP = u'I'
    EXPERIENCE = u'E'
    PROGRAM_CHOICES = (
        (FELLOWS, 'Fellows'),
        (CTO, 'CTO Bootcamp'),
        (INTERNSHIP, 'Interns'),
        (EXPERIENCE, 'Experience'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    alumni = models.BooleanField(default=True)
    nationality = models.CharField(max_length=255)
    current_location = models.CharField(max_length=255)
    work = models.CharField(max_length=255)
    primary_language = models.CharField(max_length=12, choices=settings.LANGUAGES)
    secondary_language = models.CharField(max_length=12, choices=settings.LANGUAGES,
                                          null=True, blank=True)
    additional_language = models.CharField(max_length=12, choices=settings.LANGUAGES,
                                           null=True, blank=True)
    startup_status = models.BooleanField(default=False)
    portfolio_status = models.BooleanField(default=False)
    itc_program_name = models.CharField(max_length=1,
                                        choices=PROGRAM_CHOICES,
                                        default=EXPERIENCE)
    itc_program_year = models.IntegerField(default=2013, validators=[MinValueValidator(2013),
                                                                     MaxValueValidator(2016)])
    itc_program_cohort = models.CharField(max_length=4, choices=tuple((m, m) for m in calendar.month_abbr[1:]),
                                          default='Jan')
    linked_in_url = models.CharField(max_length=255, default='http://linkedin.com/')
    cluster = models.IntegerField(default=0)
    skills = TaggableManager(blank=True)

    class Meta:
        verbose_name_plural = 'User Profiles'
        verbose_name = 'User Profile'

    def __unicode__(self):
        return u'%s: Profile' % self.user.email
