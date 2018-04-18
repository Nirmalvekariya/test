from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import UserProfile
from django.forms import ModelForm

rio_choices = [
    ('','Select your Role in Organization'),
    ('executive', 'Executive'),
    ('admin', 'Admin'),
    ('student', 'Student'),
]

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(required=True)
    organisation_id = forms.CharField(max_length=100)
    role_in_organisation = forms.CharField(widget=forms.Select(choices=rio_choices))
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'organisation_id',
            'role_in_organisation',
            'password1',
            'password2',
        ]


    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.oid = self.cleaned_data['organisation_id']
        user.rio = self.cleaned_data['role_in_organisation']
        #user.password1=(self.cleaned_data["password1"])

        if commit:
            user.save()
        return user
