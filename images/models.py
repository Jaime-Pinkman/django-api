from django.db import models
from PIL import Image


class Photo(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pictures')