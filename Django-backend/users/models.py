from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserAccountManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError("User must have an email address")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save()

        return user

    # def create_superuser(self, email, name, password):
    #     user = self.create_user(email, name, password)

    #     user.is_superuser = True
    #     user.is_staff = True
    #     user.save()

    #     return user


class UserAccount(AbstractBaseUser, PermissionError):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True) # is_active is required for custom user model
    is_staff = models.BooleanField(default=False) # is_staff is required for custom user model

    objects = UserAccountManager()


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.email
