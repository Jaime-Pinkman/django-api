from rest_framework.response import Response
from images.models import Photo
from rest_framework.views import APIView
from images.face_recognizer import FaceRecognizer
from scipy.spatial import distance


"""class CheckImageView(APIView):
    def post(self, request):
        file = request.data.get('file', None)
        if file:
            image = Photo.objects.create(image=file)
            face = find_save_face(image.image.path)
            image.delete()
            if face is not None:
                face_thresh = 0.6
                start_point = 100
                faces = Photo.objects.all()
                index = -1
                for i in range(len(faces)):
                    if faces[i].portrait != '':
                        dist = distance.euclidean(list(map(float, faces[i].portrait.split(','))), face.chosen["face_descriptor"])
                        if dist < start_point:
                            index = i
                            start_point = dist
                print(start_point)
                if start_point < face_thresh:
                    print(faces[index].image)
                    return Response(status=200)
                else:
                    print("A New Face!")
                    return Response(status=200)
            else:
                return Response(status=400)
        else:
            return Response(status=400)"""


class UploadView(APIView):
    def post(self, request):
        file = request.data.get('file', None)
        if file:
            try:
                user_frame = FaceRecognizer(file)
            except Exception:
                return Response(status=400)
            Photo.objects.create(image=file, portrait=str(user_frame.portrait).replace("\n", ",")) #
            return Response(status=200)
        else:
            return Response(status=400)