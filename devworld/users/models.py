from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
# Create your models here.

JOB_OPTIONS = [
    ('Backend','BACKEND'),
    ('Frontend','FRONTEND'),
    ('Fullstack','FULLSTACK'),
    ('Data','DATA'),
    ('Devops','DEVOPS'),
]

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, blank=True, null=True )
    email = models.EmailField(max_length=200, blank=True, null=True)
    username = models.CharField(max_length=100, blank=True, null=True )
    short_intro = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    job_field = models.CharField(
        max_length=10,
        choices=JOB_OPTIONS,
        default=None,
        blank=True, null=True
    )
    social_github = models.CharField(max_length=200, blank=True, null=True)
    social_website = models.CharField(max_length=200, blank=True, null=True)
    social_linkedin = models.CharField(max_length=200, blank=True, null=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='profiles/', default='profiles/default_user.jpeg')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.username)


class Technology(models.Model):
    owner = models.ForeignKey(
        Profile, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, blank=True, null=True )
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

class Message(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    recipient = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True, related_name="messages")
    name = models.CharField(max_length=200,null=True,blank=True)
    body = models.TextField()
    is_read = models.BooleanField(default=False,null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['is_read', '-created']
