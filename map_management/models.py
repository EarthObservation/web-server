from django.conf import settings
from django.db import models
from django.contrib.auth.models import Group, User


class UserMap(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    map_title = models.CharField(max_length=50)


class GroupMap(models.Model):

    group = models.ForeignKey(Group)

    map_title = models.CharField(max_length=50)


