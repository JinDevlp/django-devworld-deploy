from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver

from django.contrib.auth.models import User
from .models import Profile

from django.core.mail import BadHeaderError, send_mail
from django.conf import settings
# from django.http import HttpResponse, HttpResponseRedirect
# Need to make changed to apps.py for these signals


"""Create a Profile when creating a User"""
# @receiver(post_save, sender=Profile)
def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user = user,
            username = user.username,
            email = user.email,
            name = user.first_name,
        )

        subject = "Welcome to Devworld"
        message = "You have signed up with us to join the IT community!"

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False,

        )

"""this will update User info when Profile info is updated"""
def updateUser(sender,instance,created, **kwargs):
    profile = instance
    user = profile.user

    if created == False: # Make sure user is not created
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()



"""Delete the User when deleting a Profile"""
# @receiver(post_delete, sender=Profile)
def deleteUser(sender,instance, **kwargs):
    user = instance.user
    user.delete()
    print("Deleting User...")


post_save.connect(createProfile,sender=User)
post_save.connect(updateUser,sender=Profile)
post_delete.connect(deleteUser,sender=Profile)