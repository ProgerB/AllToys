from django.db import models
import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils import timezone
from toys.enums import ToyTypeEnum


class ActiveObjectManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


# class BaseModel(models.Model):
#     is_active = models.BooleanField(default=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         abstract = True


class Address(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100, null=True, blank=True)
    zip_code = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.street


class User(AbstractUser):
    # is_active = models.BooleanField(default=True)
    # first_name = models.ChasrField(max_length=50)
    # last_name = models.CharField(max_length=50, null=True, blank=True)
    # email = models.EmailField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    address = models.OneToOneField(Address, on_delete=models.PROTECT, null=True, blank=True)
    # objects = models.Manager()
    # active_objects = ActiveObjectManager()

    def __str__(self):
        return self.first_name


class Tag(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Toy(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, related_name="toys", on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    type = models.CharField(max_length=ToyTypeEnum.max_length(), choices=ToyTypeEnum.get_value_tuples(),
                            null=True, blank=True)
    tags = models.ManyToManyField(Tag, related_name="toys")
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
