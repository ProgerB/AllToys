from django.db import models


class Markets(models.Model):
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=64, null=True)

    def __str__(self):
        return self.name
