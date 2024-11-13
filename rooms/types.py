import strawberry
import typing
from strawberry import auto
from . import models 
from users.types import UserType
from reviews.types import ReviewType
from django.conf import settings

@strawberry.django.type(models.Room)
class RoomType:
  id:auto
  name: auto # auto는 자동으로 model로 가서 type를 알아낸다
  kind: auto
  owner: 'UserType'

  @strawberry.field
  def reviews(self,page:int) -> typing.List['ReviewType']:
    page_size = settings.PAGE_SIZE
    start = (page - 1) * page_size
    end = start + page_size
    return self.reviews.all()[start:end]
  
  @strawberry.field
  def rating(self) -> str:
    return self.rating()