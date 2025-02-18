from rest_framework import serializers
from accounts.models import Citizen 

class CitizenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Citizen
        fields = ['first_name', 'last_name', 'city', 'address', 'blood_type', 'phone_number']
