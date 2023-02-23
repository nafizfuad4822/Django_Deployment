from django import forms
from django.contrib.auth.models import User
from Login_App.models import UserProfile

class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control mb-2'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control mb-2'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'type':'password','class':'form-control mb-2'}))
    class Meta:
        model = User 
        fields = ('username','email','password')

class UserProfileForm(forms.ModelForm):
    facebook_id = forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'form-control mb-2','type':'url'}))
    class Meta:
        model = UserProfile
        fields = ('facebook_id', 'profile_pic')

