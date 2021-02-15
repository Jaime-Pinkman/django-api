from django.urls import include, path
from rest_framework.routers import DefaultRouter
from images.views import ImageViewSet

router = DefaultRouter(trailing_slash=True)

router.register('photo', ImageViewSet, basename='photo')

urlpatterns = [
    path('', include(router.urls)),
]
