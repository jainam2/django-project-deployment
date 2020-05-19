from django import forms
from django.contrib.auth.models import User


class UserProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=64)
    last_name = forms.CharField(max_length=64)
    job_profile = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())
    password_confirmation = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        all_clean_data = super().clean()
        p = all_clean_data['password']
        pv = all_clean_data['password_confirmation']

        if p != pv:
            raise forms.ValidationError("Password entered are not same!!")

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'job_profile', 'password', 'password_confirmation']
