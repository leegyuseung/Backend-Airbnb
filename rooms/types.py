import strawberry
from strawberry import auto
from . import models 
from users.types import UserType

@strawberry.django.type(models.Room)
class RoomType:
  id:auto
  name: auto # auto는 자동으로 model로 가서 type를 알아낸다
  kind: auto
  owner: 'UserType'
