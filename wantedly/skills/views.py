# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User 
from skills.models import Skill, SkillSet, Endorsement
from django.shortcuts import render, redirect
from skills.forms import AddSkillForm

def user_profile(request, user_pk, user_profile_pk):
	active_user = User.objects.get(pk=user_pk)
	profile_user = User.objects.get(pk=user_profile_pk)
	skill_sets = SkillSet.objects.filter(user_key=user_profile_pk)

	# endorsements that the current user has given to this profile 
	endorsements = Endorsement.objects.all().filter(user_endorsing=active_user, user_endorsed=profile_user)

	# an array to keep track of if any of the skills are endorsed by this active user,
	# which would disable the endorse button 
	endorsed = []
	if endorsements:
		i = 0
		for skill_set in skill_sets:
			if (skill_set == endorsements[i]):
				endorsed.append(1)
				i = i + 1 
				print ("endorsement matches!")
			else:
				endorsed.append(0)
	else:
		for skill_set in skill_sets:
			endorsed.append(0)

	print ('endorsed', endorsed)


	if request.method == "POST":
		form = AddSkillForm(request.POST)

		if form.is_valid():
			# add new skill to user's profile
			pass

	else:
		form = AddSkillForm()


	#skill_sets_zipped = zip(skill_sets, endorsed)
	
	args = {
		'profile_user' : profile_user,
		'skill_sets' : skill_sets,
		#'skill_sets' : skill_sets_zipped, 

		# TODO: FIX WHY I RUN INTO REVERSE ERRORS IF I UNCOMMENT THE ABOVE 

		'form': form
	}	

	return render(request, 'skills/profile.html', args)

def user_list(request):
	users = User.objects.all()

	args = {
		'users': users 
	}

	return render(request, 'skills/user_list.html', args)

def endorse(request, user_pk, user_profile_pk, skill_set_pk):

	skill_set = SkillSet.objects.get(pk=skill_set_pk)
	skill_set.endorsements = skill_set.endorsements + 1 
	skill_set.save()

	# create new endorsment object with the user_pk and user_profile pk

	endorsee = User.objects.get(pk=user_pk)
	endorsed = User.objects.get(pk=user_profile_pk)

	endorsement = Endorsement(user_endorsing=endorsee,user_endorsed=endorsed, endorsed_skill_set=skill_set)
	print(endorsement)
	endorsement.save()

	return redirect('user_profile', user_pk=user_pk, user_profile_pk=user_profile_pk)
