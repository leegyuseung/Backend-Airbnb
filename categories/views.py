from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.status import HTTP_202_ACCEPTED
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import Category
from .serializers import CategorySerializer

class CategoryViewSet(ModelViewSet):

  serializer_class = CategorySerializer
  queryset = Category.objects.filter(kind=Category.CategoryKindChoices.ROOMS)
 