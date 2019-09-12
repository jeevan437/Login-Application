from django import forms
from .models import DjUser


class SignUpForm(forms.ModelForm):

    username = forms.CharField(max_length=30, required=True, label="UserName")
    email = forms.EmailField(max_length=255, required=True, label="Email")
    first_name = forms.CharField(max_length=30, required=True, label='FirstName')
    last_name = forms.CharField(max_length=30, required=True, label='LastName')
    password = forms.CharField(max_length=30, required=True, label='Password', widget=forms.PasswordInput())

    class Meta:

        model = DjUser
        fields = ('department', 'branch', 'gender', 'rollno', 'doj', 'dob', 'phone_num', 'address')