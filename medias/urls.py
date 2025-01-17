from django.urls import path
from .views import photoDetail, GetUploadURL

urlpatterns = [
  path('photos/get-url', GetUploadURL.as_view()),
  path('photos/<int:pk>', photoDetail.as_view()),
]
