from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="image", null=True)
    Description = models.CharField(max_length=25000)
    image = models.ImageField(upload_to="img/%y")
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    def __str__(self):
        return self.Description

