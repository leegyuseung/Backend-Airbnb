from rest_framework.test import APITestCase
from . import models
from users.models import User
class TestAmenities(APITestCase):

  NAME = "Amenity Test"
  DESC = "Amenity Des"
  URL = "/api/v1/rooms/amenities/"

  # 다른 모든 test들이 실행하기 전에 실행
  def setUp(self) -> None:
    models.Amenity.objects.create(
      name=self.NAME,
      description=self.DESC
    )
  
  def test_all_amenities(self):
    
   response= self.client.get(self.URL)
   data = response.json()

   self.assertEqual(response.status_code,200,"Status code isn`t 200.")
 
   self.assertIsInstance(data, list)

   self.assertEqual(len(data),1)
   self.assertEqual(data[0]["name"], self.NAME)
   self.assertEqual(data[0]["description"], self.DESC)

  def test_create_amenity(self):
   
   new_amenity_name = "New Amenity"
   new_amenity_description = "New Amenity description"

   response = self.client.post(self.URL, data={"name":new_amenity_name, "description":new_amenity_description})
   data = response.json()

   self.assertEqual(response.status_code, 200, "Not 200 status code")
   self.assertEqual(data['name'], new_amenity_name)
   self.assertEqual(data['description'], new_amenity_description)

   response = self.client.post(self.URL)
   data = response.json()
   self.assertEqual(response.status_code, 400)
   self.assertIn("name", data)

class TestAmenity(APITestCase):

  NAME = "Test Amenity"
  DESC = "Test Desc"

  def setUp(self):
    models.Amenity.objects.create(
      name = self.NAME,
      description = self.DESC
    )

  def test_amenity_not_found(self):
    response = self.client.get("/api/v1/rooms/amenities/2")

    self.assertEqual(response.status_code, 404)

  def test_get_amenity(self):

    response = self.client.get("/api/v1/rooms/amenities/1")

    self.assertEqual(response.status_code, 200)

    data = response.json()

    self.assertEqual(data['name'], self.NAME)
    self.assertEqual(data['description'], self.DESC)

  def test_put_amenity(self):
    pass

  def test_delete_amenity(self):

    response = self.client.delete("/api/v1/rooms/amenities/1")
    self.assertEqual(response.status_code, 204)
 
class TestRoom(APITestCase):

  def setUp(self):
    user = User.objects.create(
      username="testtest"
    )
    user.set_password('1234')
    user.save()
    self.user = user

  def test_create_room(self):
    
    resposne = self.client.post('/api/v1/rooms/')
    self.assertEqual(resposne.status_code, 403)
 
    self.client.force_login(
      self.user
    )

    resposne = self.client.post('/api/v1/rooms/')