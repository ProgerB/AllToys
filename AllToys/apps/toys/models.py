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


class BaseModel(models.Model):
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Address(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100, null=True, blank=True)
    zip_code = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Address"

    def __str__(self):
        return self.street


class User(AbstractUser, BaseModel):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    address = models.OneToOneField(Address, on_delete=models.PROTECT, null=True, blank=True)

    # class Meta:
    #     db_table = "user"
    #     verbose_name_plural = "Users"

    def __str__(self):
        if self.last_name:
            return f"{self.last_name} {self.first_name}"
        return self.first_name


class Tag(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


def photo_upload_path(instance, filename):
    current_dt = timezone.now()
    return f"toy-photos/{current_dt.strftime('%Y_%m')}/{uuid.uuid4().hex}/{filename}"


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

    # def get_absolute_url(self):
    #     return reverse("toys:toy_detail", args=(self.id,))
    #
    # class Meta:
    #     verbose_name_plural = "Toys"


class Employee(User):
    experience = models.IntegerField(null=True, blank=True)
    salary = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Employees"

    def __str__(self):
        return self.first_name + " " + self.last_name


class Company(models.Model):
    company_name = models.CharField(max_length=64)
    company_email = models.EmailField(max_length=50, null=False, blank=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)
    employees = models.ManyToManyField(Employee, related_name="Company")

    def __str__(self):
        return self.company_name