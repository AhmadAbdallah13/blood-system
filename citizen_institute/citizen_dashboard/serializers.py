from rest_framework import serializers
from .models import KhaldaHospitalAppointment, BloodDonationAppointment
from institute_dashboard.models import UrgentCaseList

class KhaldaHospitalAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = KhaldaHospitalAppointment
        fields = '__all__'


class UrgentCaseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrgentCaseList
        fields = "__all__"
        
        
        
class BloodDonationAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model= BloodDonationAppointment
        fields= '__all__'
    def validate(self, data):
        """
        Custom validation to ensure:
        - Users who donated in the last 2 months can't donate now.
        - Donation units can only be selected if donation is allowed.
        """
        if data.get('donated_last_two_months'):
            raise serializers.ValidationError("You cannot donate now. Please wait at least 2 months.")
        if not data.get('donated_last_two_months') and not data.get('donation_units'):
            raise serializers.ValidationError("Please select the number of donation units.")
        return data