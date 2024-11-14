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
    Policy_id = serializers.IntegerField(source = "policy_id")
    Date_of_Purchase = serializers.CharField(source="date_of_purchase")
    Customer_id = serializers.IntegerField(source = "customer_id")
    Fuel = serializers.CharField(source = "fuel")
    VEHICLE_SEGMENT = serializers.CharField(source = "vehicle_segment")
    Premium = serializers.IntegerField(source = "premium")
    bodily_injury_liability = serializers.IntegerField()
    personal_injury_protection = serializers.IntegerField()
    property_damage_liability = serializers.IntegerField()
    collision = serializers.IntegerField()
    comprehensive = serializers.IntegerField()
    Customer_Gender = serializers.CharField(source = "customer_gender")
    Customer_Income_group = serializers.CharField(source = "customer_income_group")
    Customer_Region = serializers.CharField(source = "customer_region")
    Customer_Marital_status = serializers.IntegerField(source = "customer_marital_status")
        