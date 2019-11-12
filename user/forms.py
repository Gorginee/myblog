from django import forms
from django.core.exceptions import ValidationError
from django.forms import Form


class RegisterForm(Form):
    username = forms.CharField(max_length=20, error_messages={'required': 'Usernane is required.', 'max_length': 'The length of username can not more than 20.'})
    password = forms.CharField(widget=forms.widgets.PasswordInput, min_length=6, max_length=18, error_messages={'min_length': 'The lengh of password can not smaller than 6.', 'max_length': 'The lengh of password can not greater than 18.'})
    confirm = forms.CharField(widget=forms.widgets.PasswordInput)

    def clean_confirm(self):
        if not self.cleaned_data.get('confirm') == self.cleaned_data.get('password'):
            raise ValidationError('The two password is not consistent.')

