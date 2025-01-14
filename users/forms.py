from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    user_type = forms.ChoiceField(choices=UserProfile.USER_TYPE_CHOICES)
    profile_picture = forms.ImageField()
    address_line1 = forms.CharField(max_length=100)
    city = forms.CharField(max_length=50)
    state = forms.CharField(max_length=50)
    pincode = forms.CharField(max_length=6)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add form-control class to all fields
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
        
        # Custom help texts for password fields
        self.fields['password1'].help_text = 'Your password must contain at least 8 characters.'
        self.fields['password2'].help_text = 'Enter the same password as before, for verification.'

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        
        if password1 and password2 and password1 != password2:
            self.add_error('password2', "The two password fields didn't match. Please try again.")
            raise forms.ValidationError("The two password fields didn't match.")

        return cleaned_data

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email is already registered.')
        return email

    def clean_pincode(self):
        pincode = self.cleaned_data.get('pincode')
        if not pincode.isdigit() or len(pincode) != 6:
            raise forms.ValidationError('Pincode must be 6 digits')
        return pincode