from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from images import views


urlpatterns = [
    path('upload/', views.UploadView.as_view(), name='file_upload'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
