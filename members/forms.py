from django import forms
from django.core import validators


class NewMemberForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=20, validators=[validators.RegexValidator(regex='^[a-zA-Z/s]+$', message="Only letters allowed!")])
    last_name = forms.CharField(label='Last Name', max_length=20, validators=[validators.RegexValidator(regex='^[a-zA-Z/s]+$', message="Only letters allowed!")])
