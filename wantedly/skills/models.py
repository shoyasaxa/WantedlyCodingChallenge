# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class SkillSet(models.Model):
	user_key = models.ForeignKey("auth.User", on_delete=models.CASCADE)
	skill = models.ForeignKey("Skill", on_delete=models.CASCADE)
	endorsements = models.PositiveSmallIntegerField(default=0)

	def __str__(self):
		return str(self.user_key) + " " + str(self.skill) + " " + str(self.endorsements)

class Skill(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name