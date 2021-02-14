from django.db import models


class Photo(models.Model):
    portrait = models.TextField()
    image = models.ImageField(upload_to='pictures')
