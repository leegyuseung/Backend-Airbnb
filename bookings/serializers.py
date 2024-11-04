from django.utils import timezone
from rest_framework import serializers
from .models import Booking

class CreateRoomBookingSerializer(serializers.ModelSerializer):

  check_in = serializers.DateField()
  check_out = serializers.DateField()

  class Meta:
    model = Booking
    fields =(
      "check_in",
      "check_out",
      "guests",
    )

  # validation 해준다
  # validate + _field name
  def validate_check_in(self, value):
    now = timezone.localtime(timezone.now()).date()
    if now > value:
      raise serializers.ValidationError('Can`t book in the past!')
    return value

  def validate_check_out(self, value):
    now = timezone.localtime(timezone.now()).date()
    if now > value:
      raise serializers.ValidationError('Can`t book in the past!')
    return value

  def validate(self, data):
    if data['check_out'] < data['check_in']:
     raise serializers.ValidationError('Check in should be smaller than check out.')

    # 날짜가 겹치는 예약을 감지하지 못함
    # Booking.objects.filter(check_in__gte=data['check_in'],check_out__lte=data['check_out']).exists()
    if Booking.objects.filter(check_in__lte=data['check_out'],check_out__gte=data['check_in']).exists():
      raise serializers.ValidationError('Those (or some) of those dates are alrady token.')

    return data

# 모두가볼수있는 공개적인 booking serializer
class PublicBookingSerializer(serializers.ModelSerializer):

  class Meta:
    model = Booking
    fields = (
      "pk",
      "check_in",
      "check_out",
      "experience_time",
      "guests"
    )