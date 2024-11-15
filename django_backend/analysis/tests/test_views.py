from django.test import TestCase
from ..views.api_views import *
from django.urls import reverse
from rest_framework import status


class BatchDataUploadViewTest(TestCase):
    def setUp(self):
        self.valid_data = {
            "Policy_id": 12345,
            "Date_of_Purchase": "1/16/2018",
            "Customer_id": 400,
            "Fuel": "CNG",
            "VEHICLE_SEGMENT": "A",
            "Premium": 958,
            "bodily_injury_liability": 0,
            "personal_injury_protection": 0,
            "property_damage_liability": 0,
            "collision": 1,
            "comprehensive": 1,
            "Customer_Gender": "Male",
            "Customer_Income_group": "0- $25K",
            "Customer_Region": "North",
            "Customer_Marital_status": 0
        }

        self.url = reverse("batch_data_upload")
    
    def test_temp_data_creation(self):
        """Mock an API request to the temporary batch data file creation"""
        response = self.client.post(self.url, self.valid_data, content_type = "application/json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        