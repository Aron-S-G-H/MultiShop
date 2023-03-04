from django import forms
from django.core import validators
from userModel_app.models import User


# if you want to use Way2 import the module below ==>
# from django.core.exceptions import ValidationError


# Custome Validation ==>
def phone_number_validator(value):
    if value[0] != '0' and value[0:3] != '+98':
        raise forms.ValidationError('Please enter valid phone number !!')


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

# Way 2 for validating phone number ==>
# def clean_phone(self):
#     phone = self.cleaned_data.get('phone')
#     if len(phone) > 11 or len(phone) < 11 :()
#         raise ValidationError(
#             'Invalid Value: %(value)s is invalid',
#             code='Invalid',
#             params={'value': f'{phone}'}
#         )
#     return phone


class RegisterForm(forms.Form):
    fullname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}))

    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
                             validators=[validators.EmailValidator()])

    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
                            validators=[validators.MaxLengthValidator(11),
                                        validators.MinLengthValidator(11),
                                        phone_number_validator])

    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    conf_pass = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'placeholder': 'Password Confirm'}))


class CheckOtpForm(forms.Form):
    code = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Code'}),
                           validators=[validators.MaxLengthValidator(4),
                                       validators.MinLengthValidator(4)])


class EditAccountForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'phone', 'fullname')
