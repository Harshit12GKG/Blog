from __future__ import print_function
from pickle import FALSE
from django.conf import settings
from .models import *
from django.utils.text import slugify
import string,random
import time
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint

def generate_random_string(N):
    res = ''.join(random.choices(string.ascii_uppercase +
                                string.digits, k=N))
    return res

def generate_slug(text):
    new_slug = slugify(text)
    from .models import BlogModel
    if BlogModel.objects.filter(slug = new_slug).exists():
        return generate_slug(text + generate_random_string(5))
    return new_slug

from django.conf import settings
from django.core.mail import send_mail

def send_mail_to_user(token, email):
    try:
        subject = "Your Account needs to be verified"
        message = f"Hi there! Paste the link to verify your Account. The link is: http://127.0.0.1:8000/verify/{token}"
        from_email = settings.EMAIL_HOST_USER
        recipient_list =  [email]
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        return True

    except Exception as e:
        print(e)
