import csv
import os

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from core.models import UserProfile


class Command(BaseCommand):
    help = 'Imports users from input'

    def add_arguments(self, parser):
        parser.add_argument('filepath', type=str)

    def handle(self, *args, **options):
        filepath = options['filepath']
        self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % filepath))
        print os.path.exists(filepath)
        file = open('data_alumni_clusters.csv', 'rb')
        csvreader = csv.reader(file)
        next(csvreader, None)
        for row in csvreader:
            user = None
            try:
                user = UserProfile.objects.get(user__email=row[6])
                user.cluster = row[10]
                user.save()
            except:
                self.stdout.write(self.style.NOTICE('Could not create profile "%s"' % row[6]))
