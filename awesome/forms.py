from django import forms
from .models import *


class MultiTagQueryForm(forms.Form):
	tag = forms.ModelMultipleChoiceField(queryset=Tag.objects.all())
	# Platform = forms.ModelMultipleChoiceField(queryset=Tag.objects.filter(type__exact='2'))
