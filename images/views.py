from rest_framework.response import Response
from images.models import Photo
from rest_framework.views import APIView
from images.Frame import Frame


class UploadView(APIView):
    def post(self, request):
        file = request.data.get('file', None)
        if file:
            image = Photo.objects.create(image=file)
            userFrame = Frame(path=image.image.path)
            userFrame.takeVector()
            userFrame.takeBiggestFace()
            print([userFrame.chosen["rect"]])
            result = str(userFrame.chosen["face_descriptor"]).replace("\n", ",")
            print(result)
            return Response(status=200)
        else:
            return Response(status=400)