from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from .models import PasswordHistory

# Custom password change form (for password history check)
class CustomPasswordChangeForm(PasswordChangeForm):
    def clean_new_password1(self):
        new_password = self.cleaned_data['new_password1']
        user = self.user
        recent_passwords = PasswordHistory.objects.filter(user=user).order_by('-changed_at')[:3]
        for p in recent_passwords:
            if check_password(new_password, p.hashed_password):
                raise forms.ValidationError("You cannot reuse one of your last 3 passwords.")
        return new_password

# Custom signup form with only username, email, and password
class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
