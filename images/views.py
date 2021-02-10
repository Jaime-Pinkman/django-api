from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from images.models import Photo
from images.serializers import PhotoSerializer
from snippets.serializers import SnippetSerializer
from rest_framework.views import APIView
from django.http import Http404, HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser, FileUploadParser
import json
from PIL import Image
from images.Frame import Frame


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    def post(self, request, *args, **kwargs):
        file = request.data['file']
        image = Photo.objects.create(image=file)
        return HttpResponse(json.dumps({'message': "Uploaded"}), status=200)


class UploadView(APIView):
    #parser_classes = (FileUploadParser)

    def post(self, request):
        file = request.data.get('file', None)
        #print(file)
        if file:
            img = Image.open(file)
            userFrame = Frame(path=file)
            userFrame.takeVector()
            userFrame.takeBiggestFace()
            print([userFrame.chosen["rect"]])
            result = str(userFrame.chosen["face_descriptor"]).replace("\n", ",")
            print(result)
            image = Photo.objects.create(image=file)
            return Response(status=200)
        else:
            return Response(status=400)


"""class ProductViewSet(BaseViewSet, viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @detail_route(methods=['post'])
    def upload_docs(request):
        try:
            file = request.data['file']
        except KeyError:
            raise ParseError('Request has no resource file attached')
        product = Product.objects.create(image=file, ....)"""