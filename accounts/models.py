from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    following = models.ManyToManyField('self', related_name="followers", symmetrical=False)
    profile_photo = models.ImageField(upload_to='images/', blank=True)