from django.conf.urls import url

from .views import UserMaps

urlpatterns = [
    url(r'^$', UserMaps.as_view(), name='index'),
]
