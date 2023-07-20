from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="Email",
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    mobile = forms.CharField(label="Mobile",
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter mobile number'}))
    country = forms.ChoiceField(label="Country",
                                choices=(
                                    ('Kenya', 'Kenya'),
                                    ('Uganda', 'Uganda'),
                                    ('Tanzania', 'Tanzania'),
                                    # Add more country options here
                                ),
                                widget=forms.Select(attrs={'class': 'form-select', 'id': 'inputGroupSelect01'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'mobile', 'country')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = 'Enter username'
        self.fields[
            'username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Enter Password'
        self.fields['password1'].label = 'Password'
        self.fields[
            'password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = 'Confirm password'
        self.fields[
            'password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'
