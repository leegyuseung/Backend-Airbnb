from django.db import models

# 데이터베이스에 추가되지 않을 모델
class CommonModel(models.Model):

  """Common Model Definition"""
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at= models.DateTimeField(auto_now=True)

  class Meta:
    abstract = True
  