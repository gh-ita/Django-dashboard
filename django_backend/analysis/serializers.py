from rest_framework import serializers 
from .models import Customer, Policy

class CustomerSerializer(serializers.ModelSerializer):
    class Meta :
        model = Customer
        fields = ["customer_id", "gender", "region"]

class PolicySerializer(serializers.ModelSerializer) :
    customer = CustomerSerializer()
    class Meta :
        model = Policy
        fields = ["policy_id", "customer_id", "premium", "collision", "comprehensive"]
    