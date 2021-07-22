from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Image(models.Model):
    Description = models.CharField(max_length=25000)
    image = models.ImageField(upload_to="img/%y")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.Description
