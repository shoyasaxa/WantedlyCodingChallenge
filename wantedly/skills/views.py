# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User 
from skills.models import Skill, SkillSet
from django.shortcuts import render
from skills.forms import AddSkillForm

# Create your views here.
def user_profile(request, pk):
	user = User.objects.get(pk=pk)
	skill_sets = SkillSet.objects.all().filter(user_key=pk)

	if request.method == "POST":
		form = AddSkillForm(request.POST)

		if form.is_valid():
			# add new skill to user's profile
			pass

	else:
		form = AddSkillForm()

	args = {
		'user' : user,
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