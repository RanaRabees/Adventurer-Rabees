from django.db import models

# Create your models here.
class Contactform(models.Model):
    myname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=64)
    bio = models.TextField(max_length=64)
    images = models.ImageField(upload_to = "images" ,default="")

    def __str__(self):
        return self.myname


