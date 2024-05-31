from django.db import models
from django.contrib.auth.models import User
import uuid

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    college_location = models.CharField(max_length=200, blank=True, null=True)
    home_location = models.CharField(max_length=200, blank=True, null=True)
    short_intro = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(max_length=200, blank=True, null=True)
    through = models.ForeignKey('Skill', on_delete=models.SET_NULL, blank=True, null=True)
    profile_image = models.ImageField(blank=True, null=True, upload_to='profiles/', default="profiles/default.jpg")
    instagram = models.CharField(max_length=200, blank=True, null=True)
    linkdin = models.CharField(max_length=200, blank=True, null=True)
    phone_number = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=4, primary_key=True, editable=False)

    def __str__(self):
        return str(self.user.username)

class Skill(models.Model):
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=4, primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)
# Create your models here.
