from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Technology, Message

class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']

class ProfileForm(ModelForm):

    class Meta:
        model = Profile
        fields = ['name','email','username','short_intro','bio','job_field','social_github','social_website','social_linkedin','profile_image']

class TechnologyForm(ModelForm):

    class Meta:
        model= Technology
        fields = '__all__'
        exclude= ['owner']


class MessageForm(ModelForm):

    class Meta:
        model= Message
        fields = '__all__'
        exclude = ['sender','recipient','is_read','created']