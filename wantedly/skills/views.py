# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User 
from skills.models import Skill, SkillSet
from django.shortcuts import render, redirect
from skills.forms import AddSkillForm

# Create your views here.
def user_profile(request, pk):
	profile_user = User.objects.get(pk=pk)
	skill_sets = SkillSet.objects.all().filter(user_key=pk)

	if request.method == "POST":
		form = AddSkillForm(request.POST)

		if form.is_valid():
			# add new skill to user's profile
			pass

	else:
		form = AddSkillForm()

	args = {
		'profile_user' : profile_user,
		'skill_sets' : skill_sets, 
		'form': form
	}	

	return render(request, 'skills/profile.html', args)

def user_list(request):
	users = User.objects.all()

	args = {
		'users': users 
	}

	return render(request, 'skills/user_list.html', args)

def endorse(request, user_profile_pk, skill_set_pk):
	
	# need to expand user model to include which skill for which person a user has
	# already endorsed

	skill_set = SkillSet.objects.get(pk=skill_set_pk)
	print(skill_set)
	print(skill_set.endorsements)
	print(skill_set.skill)
	skill_set.endorsements = skill_set.endorsements + 1 
	skill_set.save()

	return redirect('user_profile', pk=user_profile_pk)
