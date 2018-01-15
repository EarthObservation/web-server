from allauth.account import app_settings as allauth_settings
from allauth.utils import email_address_exists
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from rest_auth.serializers import UserDetailsSerializer
from .models import UserProfile
from django.contrib.auth import get_user_model
from rest_framework.serializers import ValidationError, ModelSerializer
from django.contrib.auth.models import User
import re

class MyRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    password1 = serializers.CharField(write_only=True)
    password2 = password1


    def validate(self, data):
        return data

    def get_cleaned_data(self):
        super(MyRegisterSerializer, self).get_cleaned_data()
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'email': self.validated_data.get('email', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'institution': self.validated_data.get('institution', '')

        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        setup_user_email(request, user, [])
        user.save()
        return user

class MyUserProfileSerializer(ModelSerializer):
    institution = serializers.CharField()

    class Meta:
        model = UserProfile

    def create(self, validated_data):
        obj = UserProfile.objects.create(**validated_data)
        obj.save(foo=validated_data['foo'])
        return obj
