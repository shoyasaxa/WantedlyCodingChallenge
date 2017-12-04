from django import forms
from skills.models import Skill

skills = Skill.objects.all()
SKILL_CHOICES = []
for skill in skills:
	SKILL_CHOICES.append(skill.name)


class AddSkillForm(forms.Form):
	skills = forms.MultipleChoiceField(
		required=False,
		widget= forms.CheckboxInput,
		choices=SKILL_CHOICES
	)
