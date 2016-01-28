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
        program_lookup = {'Bootcamp': 'B', 'Experience': 'E', 'Fellows': 'F', 'Interns': 'I'}
        filepath = options['filepath']
        self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % filepath))
        print os.path.exists(filepath)
        file = open('itc.csv', 'rb')
        csvreader = csv.reader(file)
        next(csvreader, None)
        for row in csvreader:
            user = None
            try:
                user = User.objects.create(username=row[6],
                                           first_name=row[3],
                                           last_name=row[4],
                                           email=row[6],
                                           password='password1234')
            except:
                user = User.objects.get(email=row[6])
                self.stdout.write(self.style.NOTICE('Could not create user "%s"' % row[6]))
            try:
                if row[1] == '2015' and row[2] == 'October':
                    UserProfile.objects.create(user=user,
                                               alumni=False,
                                               nationality=row[5],
                                               current_location='TEL AVIV',
                                               primary_language='en',
                                               itc_program_year=int(row[1]),
                                               itc_program_name=program_lookup[row[0]])
                else:
                    UserProfile.objects.create(user=user,
                                               alumni=True,
                                               nationality=row[5],
                                               current_location='TEL AVIV',
                                               primary_language='en',
                                               itc_program_year=int(row[1]),
                                               itc_program_name=program_lookup[row[0]])
            except:
                self.stdout.write(self.style.NOTICE('Could not create profile "%s"' % row[6]))
