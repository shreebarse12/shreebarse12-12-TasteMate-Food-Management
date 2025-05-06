from .models import Tweet
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture', 'bio']
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class TweetForm(forms.ModelForm):
     class Meta:
                model = Tweet
                fields = ['text', 'photo']
                
class userRegistrationForm(UserCreationForm):
    class meta:
        model = Tweet
        fields = ('username', 'email', 'password1', 'password2')

        