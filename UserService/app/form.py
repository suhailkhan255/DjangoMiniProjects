from django import forms
from .models import CustomUser


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['profile_picture', 'first_name', 'last_name', 'email', 'phone_number', 'nationality',
                  'pan_number', 'gstin_number']
