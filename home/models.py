from lib2to3.pgen2 import token
from operator import mod
from pyexpat import model
from statistics import mode
from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField
from django.contrib import admin
from sqlalchemy import BLANK_SCHEMA, false
from . helpers import generate_slug, generate_random_string
# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    is_verifified = models.BooleanField(default=False)
    token = models.CharField(max_length=100)

    def __str__(self):
        return self.token


class BlogModel(models.Model):
    title = models.CharField(max_length=1000)
    content = FroalaField()
    slug = models.SlugField(max_length=1000, null=True, blank=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog')
    created_at = models.DateTimeField(auto_now_add=True)
    upload_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args,**kwargs):
        self.slug = generate_slug(self.title)
        super(BlogModel, self).save(*args, **kwargs)
