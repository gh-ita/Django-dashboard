from rest_framework.exceptions import ValidationError
from rest_framework.test import APITestCase
from ..serializers import BatchDataSerializer

class BatchDataSerializerTest(APITestCase):
    def test_valid_data(self):
        valid_data = {
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

        serializer = BatchDataSerializer(data=valid_data)
        is_valid = serializer.is_valid()
        
        # Now print errors if the validation fails
        if not is_valid:
            print(serializer.errors)
        self.assertTrue(serializer.is_valid()) 
       
        self.assertEqual(serializer.validated_data['policy_id'], 12345)
