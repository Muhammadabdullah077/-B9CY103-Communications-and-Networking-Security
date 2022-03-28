from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from chat.models import Message
from chat.forms import SignUpForm
from chat.serializers import MessageSerializer
from .models import Profile
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from ChatApp import settings

ef send_email(sender):
    import random
    profile = Profile.objects.get(user=User.objects.get(email=sender.user.email))
    code = str(random.random())
    if code:
        print()
        subject = "Verification Email"
        body = {
            'subject': "Verification | DBS Chat System",
            'message': 'verification code is: ' + str(code),
        }