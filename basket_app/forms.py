from django import forms
from .models import UserOrder


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = UserOrder
        exclude = ('user', 'total_price', 'is_paid', 'created_at')
        widgets = {
            'fullname': forms.TextInput(attrs={
                'class': 'form-control',
                'name': 'fullname',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'name': 'email',
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'name': 'phone',
            }),
            'city': forms.TextInput(attrs={
                'class': 'form-control',
                'name': 'city',
            }),
            'postal_code': forms.NumberInput(attrs={
                'class': 'form-control',
                'name': 'postal_code',
            }),
            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'name': 'address',
            }),
        }

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')

        if len(phone) < 11:
            raise forms.ValidationError('The phone number must be at least 11 numbers')
        elif phone[0:3] == '+98':
            raise forms.ValidationError('Please enter valid phone number !!')
        elif phone:
            try:
                int(phone)
            except:
                raise forms.ValidationError('Please enter valid phone number !!')
        return phone
