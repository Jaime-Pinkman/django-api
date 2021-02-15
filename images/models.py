from django.db import models
from images.face_comparator import FaceComparator


class Photo(models.Model):
    portrait = models.TextField()
    image = models.ImageField(upload_to='pictures')

    @classmethod
    def search(cls, portrait):
        faces = cls.objects.all()
        if len(faces) > 0:
            face_comp = FaceComparator(portrait, faces)
            return face_comp.check_if_the_same_person()
        else:
            return False
