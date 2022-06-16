from logging import raiseExceptions
from sre_constants import SUCCESS
from django.contrib import messages
from telnetlib import STATUS
from tkinter import EXCEPTION
from urllib import response
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from . helpers import generate_random_string, send_mail_to_user
from . models import Profile

# Login View
class LoginView(APIView):

    def post(self, request):
        response = {}
        response['status'] = 500
        response['message'] = "Something Went Wrong!"

        try:
            data = request.data

            if data.get('username') is None:
                response['message'] = 'Key Username not Found!'
                raise Exception('Key Username not Found!')

            if data.get('password') is None:
                response['message'] = 'Key Password not Found!'
                raise Exception('Key Password not Found!')

            check_user = User.objects.filter(username = data.get('username')).first()

            if not Profile.objects.filter(user = check_user).first().is_verifified:
                response['message'] = "Your Profile doesn't exist"
                raise Exception['Profile not exists']

            if check_user is None:
                response['message'] = 'Invalid Username! Try Signing Up or login Again'
                raise Exception('Invalid Username!')

            user_obj = authenticate(username = data.get('username'), password = data.get('password'))

            if user_obj:
                # login the user
                login(request, user_obj)
                response['status'] = 200
                response['message'] = "Welcome!"
            else:
                response['message'] = 'Invalid Password!'
                raise Exception('Invalid Password!')


        except Exception as e:
            print(e)

        return Response(response)

LoginView = LoginView.as_view()


# Register View
class RegisterView(APIView):
    
    def post(self , request):
        response = {}
        response['status'] = 500
        response['message'] = 'Something went wrong'
        try:
            data = request.data
            
            if data.get('username') is None:
                response['message'] = 'key username not found'
                raise Exception('key username not found')
            
            if data.get('password') is None:
                response['message'] = 'key password not found'
                raise Exception('key password not found')
            
            
            check_user = User.objects.filter(username = data.get('username')).first()
            
            if check_user:
                response['message'] = 'Username already taken!'
                raise Exception('Username already taken!')
            
            user_obj = User.objects.create(email = data.get('username') , username = data.get('username'))
            user_obj.set_password(data.get('password'))
            user_obj.save()
            token = generate_random_string(20)
            Profile.objects.create(user = user_obj , token = token)
            send_mail_to_user(token , data.get('username'))
            messages.success(request, "A Verification email is being sent to your provided email address! If the email is not visible in the inbox, then check your spam box!")
            response['message'] = 'User created '
            response['status'] = 200
            
        except Exception as e:
            print(e)
            
        return Response(response)
            
                
RegisterView = RegisterView.as_view()