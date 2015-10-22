from django.db import models
from django.contrib.auth.models import User
import os
from uuid import uuid4
from core.utils import SEXES


def user_profile_picture(instance, filename):  # pylint: disable=unused-argument
    filename = filename.split('.')
    if len(filename) > 1:
        ext = filename[-1]
    else:
        ext = "png"
    return os.path.join("profile_picture", uuid4().hex + "." + ext)


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    profile_picture = models.ImageField(upload_to=user_profile_picture, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    roll_number = models.CharField(max_length=16, null=True, blank=True)
    type = models.CharField(max_length=16, null=True, blank=True)
    mobile = models.CharField(max_length=16, null=True, blank=True)
    is_alumni = models.BooleanField(default=False)
    sex = models.CharField(max_length=10, choices=SEXES, null=True, blank=True)

    def __unicode__(self):
        return self.user.username
