from django.db import models


class Markets(models.Model):
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=64, null=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Company(models.Model):
    name = models.CharField(max_length=64)
    employees = models.ManyToManyField(Employee, related_name="Company")

    def __str__(self):
        return self.name