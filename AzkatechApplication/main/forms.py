from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Vacation
# Create your forms here.

class DateInput(forms.DateInput): #Used for the Calendar UI
    input_type = 'date'

class NewUserForm(UserCreationForm): #Used for the user creation form
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class VacationForm(forms.ModelForm): #Used to add/edit vacations
    class Meta:
        model = Vacation
        exclude=['user'] #No need for user field when adding as user is already logged in.
        widgets = {
        	'start_date' : DateInput(), #Calendar UI
        	'end_date' : DateInput(), #Calendar UI
        }