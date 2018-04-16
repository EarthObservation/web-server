from django.http import JsonResponse
from django.views.generic import View

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import GroupMap, UserMap, UserProfile


class UserMaps(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        maps = set()

        for user_map in UserMap.objects.filter(user=request.user):
            maps.add(user_map.map_title)

        for group in request.user.groups.all():
            for group_map in GroupMap.objects.filter(group=group):
                maps.add(group_map.map_title)

        return Response({'maps': sorted(maps)})


class PublicMaps(View):

    def get(self, request):
        maps = set()

        # TODO: query maps for anonymous users from the database

        return JsonResponse({'maps': sorted(maps)})
