from django import forms
from . import models

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = models.UserProfile
		exclude = ['user']

	def __init__(self, *args, **kwargs):
	    super(UserProfileForm, self).__init__(*args, **kwargs)
	    self.fields['avatar'].required = False


class ChangePasswordForm(forms.Form):
	old_password = forms.CharField()
	new_password = forms.CharField()
	confirm_new_password = forms.CharField()