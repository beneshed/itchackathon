"""
	Bulk addition of resources from CSV files
	Author: Daniel Adelberg
"""

from .models import UserProfile
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

def create_user():
	User.objects.create(username=row__)
	return

def create_profiles():
	for row in csv:
		try: 
			user = User.objects.get(username=row__):
		except: #User not Found
			create_user()
			print "No user with those names"

	    nationality = row__
	    current_location = row__
	    work = row__
	    startup_status = row__
	    portfolio_status = row__
	    itc_program_name = row__
	    itc_program_year = row__
	    linked_in_url = row__
    
    	skills = TaggableManager()
    	skills.add(row__)

    profile_tuple = (user=user, 
	nationality=nationality, 
	current_location, 
	current_location=current_location, 
	work=work,
	startup_status=startup_status,
	portfolio_status=portfolio_status,
	itc_program_name=itc_program_name,
	itc_program_year=itc_program_year)

    UserProfile.objects.create(profile_tuple)
	return

if __name__ == "__main__":
	main()