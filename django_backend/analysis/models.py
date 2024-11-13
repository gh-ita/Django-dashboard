from django.db import models

    
class Customer(models.Model) :
    REGION_CHOICES = [("N", "North"),
                      ("E", "East"), 
                      ("W", "West"),
                      ("S", "South")]
    GENDER = [("M", "Male"), 
              ("F", "Female")]
    customer_id = models.IntegerField(primary_key= True)
    region = models.CharField(max_length= 7, choices = REGION_CHOICES)
    gender = models.CharField(max_length= 7, choices = GENDER)
    
    def __str__(self):
        return f"Customer, {self.customer_id}, {self.region}, {self.gender}"

class Policy(models.Model):
    CAR_TYPE = [
        ("A", "A"), 
        ("B", "B"), 
        ("C", "C")
    ]
    policy_id = models.IntegerField(primary_key= True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="policies")
    collision = models.BooleanField(default=False)
    vehicle_segment = models.CharField(max_length=1, choices= CAR_TYPE)
    
    def __str__(self) :
        return f'Policy {self.policy_id}, {self.customer_id}, {self.collision}, {self.vehicle_segment}'
    
    
