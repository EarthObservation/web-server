from django.http import JsonResponse
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from .models import UserMap, GroupMap


def index(request):
    maps = set()
    if request.user.is_authenticated:
        for user_map in UserMap.objects.filter(user=request.user):
            maps.add(user_map.map_title)

        for group in request.user.groups.all():
            for group_map in GroupMap.objects.filter(group=group):
                maps.add(group_map.map_title)

    return JsonResponse({'maps': sorted(maps)})

