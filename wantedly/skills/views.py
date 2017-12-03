# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from core.models import User
from skills.models import Skill, SkillSet
from django.shortcuts import render

# Create your views here.
def user_profile(request, pk):
	user = User.objects.get(pk=pk)

	skill_sets = SkillSet.objects.all().filter(user_key=pk)

	args = {
		'user' : user,
		'skill_sets' : skill_sets, 
	}	

	return render(request, 'skills/profile.html', args)