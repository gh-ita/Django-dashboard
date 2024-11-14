from rest_framework import serializers 
from .models import *


class PolicySerializer(serializers.ModelSerializer):
    class Meta :
        model = Policy
        fields = "__all__"

class DateSerializer(serializers.ModelSerializer):
    class Meta :
        model = Date 
        fields = "__all__"

class CustomerModel(serializers.ModelSerializer):
    class Meta :
        model = Customer
        fields = "__all__"
        
class BatchDataSerializer(serializers.Serializer):
    policy_id = serializers.IntegerField(source = "Policy_id")
    date_of_purchase = serializers.CharField(source = "Date of Purchase")
    customer_id = serializers.IntegerField(source = "Customer_id")
    fuel = serializers.CharField(source = "Fuel")
    vehicle_segment = serializers.CharField(source = "VEHICLE_SEGMENT")
    premium = serializers.IntegerField(source = "Premium")
    bodily_injury_liability = serializers.BooleanField(source = "bodily injury liability")
    personal_injury_protection = serializers.BooleanField(source = "personal injury protection")
    property_damage_liability = serializers.BooleanField(source = "property damage liability")
    collision = serializers.BooleanField(source = "collision")
    comprehensive: 1 = serializers.BooleanField(source = "comprehensive")
    customer_gender = serializers.CharField(source = "Customer_Gender")
    customer_income_group = serializers.CharField(source = "Customer_Income group")
    customer_region = serializers.CharField(source = "Customer_Region")
    customer_marital_status = serializers.BooleanField(source = "Customer_Marital_status")
        