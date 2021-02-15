from rest_framework.response import Response
from images.models import Photo
from rest_framework.views import APIView
from images.face_recognizer import FaceRecognizer
from images.face_comparator import FaceComparator


class CheckImageView(APIView):
    def post(self, request):
        file = request.data.get('file', None)
        if file:
            try:
                face_rec = FaceRecognizer(file)
            except Exception:
                return Response({'face is detected': False}, status=400)
            faces = Photo.objects.all()
            if len(faces) > 0:
                face_comp = FaceComparator(face_rec.portrait, faces)
                return Response({'exists': face_comp.check_if_the_same_person()})
            else:
                return Response({'exists': False})
        else:
            return Response(status=400)


class UploadView(APIView):
    def post(self, request):
        file = request.data.get('file', None)
        if file:
            try:
                face_rec = FaceRecognizer(file)
            except Exception:
                return Response({'face is detected': False}, status=400)
            Photo.objects.create(image=file, portrait=str(face_rec.portrait).replace("\n", ","))
            return Response({'face is detected', True}, status=200)
        else:
            return Response(status=400)
