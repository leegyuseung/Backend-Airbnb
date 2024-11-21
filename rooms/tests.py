from rest_framework.test import APITestCase
from . import models

class TestAmenities(APITestCase):

  NAME = "Amenity Test"
  DESC = "Amenity Des"

  # 다른 모든 test들이 실행하기 전에 실행
  def setUp(self) -> None:
    models.Amenity.objects.create(
      name=self.NAME,
      description=self.DESC
    )
  
  def test_all_amenities(self):
    
   response= self.client.get("/api/v1/rooms/amenities/")
   data = response.json()

   self.assertEqual(response.status_code,200,"Status code isn`t 200.")
 
   self.assertIsInstance(data, list)

   self.assertEqual(len(data),1)
   self.assertEqual(data[0]["name"], self.NAME)
   self.assertEqual(data[0]["description"], self.DESC)
