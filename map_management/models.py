from django.conf import settings
from django.db import models
from django.contrib.auth.models import Group, User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    institution = models.CharField(max_length=50)

class UserMap(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    map_title = models.CharField(max_length=50)

class GroupMap(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    map_title = models.CharField(max_length=50)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Create the UserProfile when a new User is saved"""
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
