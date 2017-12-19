from django.http import JsonResponse
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from .models import UserMap, GroupMap
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from jwt_auth.mixins import JSONWebTokenAuthMixin


class UserMaps(JSONWebTokenAuthMixin, View):


    def get(self, request):
        maps = set()

        for user_map in UserMap.objects.filter(user=request.user):
            maps.add(user_map.map_title)

        for group in request.user.groups.all():
            for group_map in GroupMap.objects.filter(group=group):
                maps.add(group_map.map_title)

        return JsonResponse({'maps': sorted(maps)})


class PublicMaps(View):


    def get(self, request):
        maps = set()

        # TODO: query maps for anonymous users from the database

        return JsonResponse({'maps': sorted(maps)})
