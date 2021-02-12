from django.db import models
from PIL import Image


class Photo(models.Model):
    portrait = models.TextField()
    image = models.ImageField(upload_to='pictures')