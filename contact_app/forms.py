from django import forms
from .models import ContactUs


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        exclude = ('user', 'created_at')
        widgets = {
            'name': forms.TextInput(attrs={
                'id': 'name',
                'class': 'form-control',
                'placeholder': 'Full Name',
                'required': 'required',
            }),
            'email': forms.EmailInput(attrs={
                'id': 'email',
                'class': 'form-control',
                'placeholder': 'Your Email',
                'required': 'required',
            }),
            'title': forms.TextInput(attrs={
                'id': 'subject',
                'class': 'form-control',
                'placeholder': 'Subject',
                'required': 'required',
            }),
            'message': forms.Textarea(attrs={
                'id': 'message',
                'class': 'form-control',
                'placeholder': 'Your Message',
                'required': 'required',
                'rows': '8',
            }),

        }
