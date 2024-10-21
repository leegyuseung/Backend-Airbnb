from django.urls import path
from .views import photoDetail

urlpatterns = [
  path('photo/<int:pk>', photoDetail.as_view()),
]
