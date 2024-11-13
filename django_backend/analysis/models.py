from django.db import models


class Customer(models.Model):
    REGION_CHOICE = [
        ("N", "North"),
        ("W", "West"),
        ("S", "South"),
        ("E", "East")
    ]
    GENDER_CHOICE = [
        ("M", "Male"),
        ("F", "Female")
    ]
    customer_id = models.IntegerField(primary_key=True)
    region = models.CharField(max_length=7, choices= REGION_CHOICE)
    gender = models.CharField(max_length=7, choices= GENDER_CHOICE)
    
    def __str__(self):
        return f'Customer {self.customer_id}, {self.region}, {self.gender}, '

class Date(models.Model):
    date_id = models.AutoField(primary_key=True)
    date = models.DateField(unique=True)
    year = models.IntegerField(max_length=4)
    month = models.IntegerField(max_length=2)
    quarter = models.IntegerField(max_length=1)
    
    def __str__(self):
        return f'Date, {self.date_id}, {self.month}, {self.year}, {self.quarter}'
    
    
    
class Policy(models.Model):
    policy_id = models.IntegerField(primary_key=True)
    date_id = models.ForeignKey(Date, on_delete=models.CASCADE, related_name= 'policies')
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="policies")
    premium = models.IntegerField()
    collision = models.BooleanField(default = False)
    comprehensive = models.BooleanField(default = False)
    
    def __str__(self):
        return f'Policy {self.policy_id}, {self.premium}, {self.customer_id}'
    