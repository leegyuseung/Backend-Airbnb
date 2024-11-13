from django.conf import settings
import strawberry
import typing
from . import models 
from wishlists.models import Wishlist
from users.types import UserType
from reviews.types import ReviewType
from strawberry import auto
from strawberry.types import Info

@strawberry.django.type(models.Room)
class RoomType:
  id:auto
  name: auto # auto는 자동으로 model로 가서 type를 알아낸다
  kind: auto
  owner: 'UserType'

  @strawberry.field
  def reviews(self,page:typing.Optional[int] = 1) -> typing.List['ReviewType']:
    page_size = settings.PAGE_SIZE
    start = (page - 1) * page_size
    end = start + page_size
    return self.reviews.all()[start:end]
  
  @strawberry.field
  def rating(self) -> str:
    return self.rating()
  
  @strawberry.field
  def is_owner(self, info:Info) -> bool: # Info type을 이용해야한다.
    print(info.context.request.user)
    return self.owner == info.context.request.user

  @strawberry.field
  def is_liked(self, info:Info) -> bool:
    return Wishlist.objects.filter(user=info.context.request.user, rooms__pk=self).exists()

