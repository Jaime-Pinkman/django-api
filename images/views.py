from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, status
from rest_framework.response import Response
from images.models import Photo
from images.serializers import PhotoSerializer


class ImageViewSet(
    mixins.CreateModelMixin,
    GenericViewSet,
):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = (AllowAny,)

    @action(
        methods=['post'],
        detail=False,
        url_path='search',
        url_name='search-by-photo',
    )
    def search(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = {
            'exists': Photo.search(serializer.data.get('portrait')),
        }

        return Response(
            data=data,
            status=status.HTTP_200_OK,
        )
