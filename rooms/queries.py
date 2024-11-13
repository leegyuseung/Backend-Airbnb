from . import models

def get_all_rooms():
  # 1번
  # if info.context.request.user.is_authenticated:
  #   return models.Room.objects.all()
  # else:
  #   raise Exception('Not auth.')
  return models.Room.objects.all()


def get_room(pk:int):
  try:
    return models.Room.objects.get(pk=pk)
  except models.Room.DoesNotExist:
    return None