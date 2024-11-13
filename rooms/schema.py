import strawberry
import typing
from . import types
from . import queries
from common.permissions import OnlyLoggedIn

@strawberry.type
class Query:
  all_rooms: typing.List[types.RoomType] = strawberry.field(resolver=queries.get_all_rooms, permission_classes=[
    OnlyLoggedIn
  ])
  room: typing.Optional[types.RoomType] = strawberry.field(resolver=queries.get_room) # RoomType이 있을수도 없을수도 있다.