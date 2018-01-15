from django.conf import settings
from django.db import models
from django.contrib.auth.models import Group, User
from django.db.models.signals import post_save


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    institution = models.CharField(max_length=50)

class UserMap(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    map_title = models.CharField(max_length=50)

class GroupMap(models.Model):
    group = models.ForeignKey(Group)
    map_title = models.CharField(max_length=50)

def create_user_profile(sender, instance, created, **kwargs):
    """Create the UserProfile when a new User is saved"""
    if created:
        profile = UserProfile()
        profile.user = instance
        profile.save()

post_save.connect(create_user_profile, sender=User)
