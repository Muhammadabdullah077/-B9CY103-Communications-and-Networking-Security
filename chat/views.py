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

def send_email(request):
    import random
    profile = Profile.objects.get(user=User.objects.get(email=request.user.email))
    code = str(random.random())
    if code:
        print()
        subject = "Verification Email"
        body = {
            'subject': "Verification | DBS Chat System",
            'message': 'verification code is: ' + str(code),
        }
        message = '\n'.join(body.values())
        sender = settings.EMAIL_HOST_USER
        recipient = [profile.user.username, ]
        try:
            send_mail(subject, message, sender, recipient)
            print("+++++++ Email Sent +++++++")
            return HttpResponse('Email Sent')
        except Exception as e:
            return HttpResponse(str(e))

    else:
        return HttpResponse('Make sure all fields are entered and valid.')


def verify(request):
    code = request.POST.get('code', None)
    if code:
        try:
            profile = Profile.objects.get(user=request.user)
            if profile.email_code == code:
                profile.is_verified = True
                profile.save()
                return redirect('chats')
            else:
                return HttpResponse('Wrong Verification Code!')
        except Exception as e:
            return HttpResponse(str(e))
    else:
        return HttpResponse('No Verification Code Found')
    return redirect('chats')
