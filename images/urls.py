from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from images import views

#router = routers.SimpleRouter()
#router.register('photo', views.UploadView)

urlpatterns = [
    #path('', include(router.urls)),
    path('upload/', views.UploadView.as_view(), name='file_upload'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
