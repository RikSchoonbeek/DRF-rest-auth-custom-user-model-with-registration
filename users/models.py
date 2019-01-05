from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    preferred_locale = models.CharField(max_length=2,
                                        blank=True,
                                        null=True)