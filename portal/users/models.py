from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    USER_TYPE_CHOICES = [
        ('admin', 'Admin'),
        ('startup', 'Startup'),
        ('mentor', 'Mentor'),
    ]
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ['user_type']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class StartupModel(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)

    founder_name = models.CharField(max_length=255)

    year_of_study = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    department = models.CharField(max_length=255)

    contact = models.CharField(max_length=255)
    linkedin = models.URLField(null=True, blank=True)
    location = models.CharField(max_length=255)

    cofounder_name = models.CharField(max_length=255, null=True, blank=True)

    startup_name = models.CharField(max_length=255)
    description = models.TextField()
    stage = models.CharField(max_length=255)
    sector = models.CharField(max_length=255)
    startup_linkedin = models.URLField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    logo = models.ImageField(upload_to='startup/logos/', null=True, blank=True)
    pitch_deck = models.FileField(upload_to='startup/pitch_decks/', null=True, blank=True)

    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.startup_name


class MentorModel(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)

    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    linkedin = models.URLField(null=True, blank=True)
    organisation = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    bio = models.TextField()

    verified = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name