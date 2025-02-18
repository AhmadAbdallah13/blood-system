from rest_framework import serializers
from .models import KhaldaHospitalAppointment
from institute_dashboard.models import UrgentCaseList

class KhaldaHospitalAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = KhaldaHospitalAppointment
        fields = '__all__'


class UrgentCaseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrgentCaseList
        fields = "__all__"