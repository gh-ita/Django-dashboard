from django.test import TestCase
from ..models import *
from django.core.exceptions import ValidationError

class DateModelTest(TestCase):
    def setUp(self):
        self.date = Date.objects.create(date = "2022-07-02", 
        year = 2023, 
        month = 7,
        quarter = 4
        )
    def test_date_creation(self):
        self.assertEqual(self.date.date, "2022-07-02")

class CustomerModelTest(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(customer_id = 23, 
                                                region = "N", 
                                                gender = "M")
    def test_region_field(self):
        self.assertEqual(self.customer.region,"N")
        
    def test_validity_of_region(self):
        self.customer.region = "N"
        try :
            self.customer.full_clean()
        except ValidationError :
            self.fail("Error value of region valid but raising error")
            
    def test_catch_invalid_region(self):
        self.customer.region = "Invalid"
        with self.assertRaises(ValidationError):
            self.customer.full_clean()
        
        
class PolicyModelTest(TestCase):
    def setUp(self):
        self.date = Date.objects.create(date = "2020-09-09")
        self.customer = Customer.objects.create(customer_id = 29)
        self.policy = Policy.objects.create(
            policy_id = 9, 
            date_id = self.date, 
            customer_id = self.customer,
            premium = 202
        )
    def test_date_to_policies(self):
        policy2 = Policy.objects.create(
            policy_id = 2,
            date_id = self.date,
            premium = 202,
            customer_id = self.customer
        )
        policies = self.date.policies.all()
        self.assertIn(policy2, policies)

    
