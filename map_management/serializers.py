import re

from allauth.account import app_settings as allauth_settings
from allauth.utils import email_address_exists
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from rest_auth.registration.serializers import RegisterSerializer
from rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from .models import UserProfile


class MyRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    institution = serializers.CharField(allow_blank=True)

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'institution': self.validated_data.get('institution', '')
        }

    def custom_signup(self, request, user):
        institution = self.cleaned_data.get('institution', '')
        UserProfile.objects.get_or_create(user=user)
        UserProfile.objects.filter(user=user).update(institution=institution)


class MyUserProfileSerializer(serializers.ModelSerializer):
    institution = serializers.CharField()

    class Meta:
        model = UserProfile
