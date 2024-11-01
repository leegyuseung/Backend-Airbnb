from rest_framework import serializers
from .models import Booking

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