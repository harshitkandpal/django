from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomerUser

class CustomerUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=15, required=False)
    address = forms.Textarea(required=False)
    role =  forms.ChoiceField(choices=CustomerUser.roleOptions, required=True)
    username = forms.CharField(max_length=150, required=True)
    profile_picture = forms.ImageField(required=False)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta(UserCreationForm.Meta):
        model = CustomerUser
        fields = ('username', 'email', 'phone_number', 'address', 'role', 'profile_picture', 'password')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomerUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Email is already in use.")
        return email
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email')
        user.phone_number = self.cleaned_data.get('phone_number')
        user.address = self.cleaned_data.get('address')
        user.role = self.cleaned_data.get('role')
        user.set_password(self.cleaned_data.get('password'))

        if 'profile_picture' in self.cleaned_data and self.cleaned_data['profile_picture']:
            user.profile_picture = self.cleaned_data['profile_picture']

        user.is_verified = False
        user.is_active = True
        if commit:
            user.save()
        return user
    
class CustomerUserChangeForm(AuthenticationForm):
    pass 