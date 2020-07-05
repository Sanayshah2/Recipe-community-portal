from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile,Subscriber

class UserModifiedForm(UserCreationForm):
    email = forms.CharField(max_length=20, label='Email-id')
    first_name = forms.CharField(max_length=20, label='First Name')
    last_name = forms.CharField(max_length=20, label='Last Name')
    
    class Meta():
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']
        


class UserEditForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name', 'email', 'username']
        
class ProfileEditForm(ModelForm):
    gender_choices={
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    }
        
    gender = forms.ChoiceField(widget=forms.RadioSelect(), choices=gender_choices)
    class Meta:
        model = Profile
        fields = ['bio', 'gender', 'image']

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields=['name','email']