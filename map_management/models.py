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
