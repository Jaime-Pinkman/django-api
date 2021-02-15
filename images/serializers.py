from rest_framework.exceptions import ValidationError
from images.face_recognizer import FaceRecognizer
from rest_framework import serializers
from images.models import Photo


class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Photo
        fields = ('image', 'portrait')
        read_only_fields = (
            'portrait',
        )

    def validate(self, attrs):
        file = attrs.get('image')
        try:
            face_rec = FaceRecognizer(file)
        except ValueError as err:
            raise ValidationError({'file': str(err)})
        portrait = str(face_rec.portrait).replace("\n", ",")
        attrs['portrait'] = portrait
        return attrs
