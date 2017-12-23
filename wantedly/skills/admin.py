# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from skills.models import SkillSet , Skill, Endorsement

# Register your models here.
admin.site.register(SkillSet)
admin.site.register(Skill)
admin.site.register(Endorsement)