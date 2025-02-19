from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from django.views.generic import TemplateView
from django.http import JsonResponse
from rest_framework.views import APIView  
from .models import KhaldaHospitalAppointment, BloodDonationAppointment
from institute_dashboard.models import UrgentCaseList
from citizen_dashboard.serializers import UrgentCaseListSerializer
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from datetime import datetime





class DashboardView(TemplateView):
    template_name = "citizen_dashboard/cdashboard.html"


class BloodTypeCheckAPIView(APIView):  
    def get(self, request):
        return render(request, "citizen_dashboard/BloodTypeCheck.html")
    
    def post(self, request):
        city = request.POST.get('city')
        hospital = request.POST.get('hospital')
        citizen_name = request.POST.get('citizen_name')
        email = request.POST.get('email')
        appointment_date = request.POST.get('appointment_date')

        if city and hospital and appointment_date and citizen_name and email:
            if hospital == "Khalda Hospital":
                appointment = KhaldaHospitalAppointment.objects.create(
                    city=city,
                    hospital=hospital,
                    citizen_name=citizen_name,
                    email=email,
                    appointment_date=appointment_date
                )
                return JsonResponse({
                    "message": "Your appointment has been reserved successfully!",
                    "appointment": {
                        "id": appointment.id,
                        "city": appointment.city,
                        "hospital": appointment.hospital,
                        "citizen_name": appointment.citizen_name,
                        "email": appointment.email,
                        "appointment_date": str(appointment.appointment_date)
                    }
                }, status=201)
            else:
                return JsonResponse({"error": "Only Khalda Hospital appointments are supported."}, status=400)
        else:
            return JsonResponse({"error": "Please fill all fields."}, status=400)
        
        

class UrgentCaseListAPIView(APIView):
    def get(self, request):
        urgent_cases = UrgentCaseList.objects.all()
        serializer = UrgentCaseListSerializer(urgent_cases, many=True)
        return JsonResponse({"urgent_cases": serializer.data}, safe=False, status=status.HTTP_200_OK)

class UrgentListView(APIView):
    def get(self, request):
        urgent_cases = UrgentCaseList.objects.all()
        return render(request, "citizen_dashboard/urgentlist.html", {"urgent_cases": urgent_cases})
        


class BloodDonationAppointmentView(APIView):
    def get(self, request):
        return render(request, "citizen_dashboard/donation_appointment.html")

    def post(self, request):
        city = request.POST.get('city')
        hospital_name = request.POST.get('hospital')
        citizen_name = request.POST.get('citizen_name')
        email = request.POST.get('email')
        appointment_date = request.POST.get('appointment_date')
        blood_type = request.POST.get('blood_type')
        chronic_disease = request.POST.get('chronic_disease')
        donated_last_two_months = request.POST.get('donated_last_two_months') == 'on'
        donation_units = request.POST.get('donation_units')
        donation_units = int(donation_units) if donation_units else None

        # Check if all required fields are provided
        if not all([city, hospital_name, citizen_name, email, appointment_date, blood_type]):
            return JsonResponse({"error": "Please fill all fields."}, status=400)

        
        if hospital_name == "Khalda Hospital":
            appointment = KhaldaHospitalAppointment.objects.create(
                city=city,
                citizen_name=citizen_name,
                email=email,
                appointment_date=appointment_date
            )
        else:
            # Fetch the hospital instance
            hospital_instance = get_object_or_404(Hospital, name=hospital_name)

            appointment = BloodDonationAppointment.objects.create(
                citizen_name=citizen_name,
                email=email,
                city=city,
                hospital=hospital_instance,
                appointment_date=appointment_date,
                blood_type=blood_type,
                chronic_disease=chronic_disease,
                donated_last_two_months=donated_last_two_months,
                donation_units=donation_units
            )

        return JsonResponse({
            "message": "Your blood donation appointment has been reserved successfully!",
            "appointment": {
                "id": appointment.id,
                "city": appointment.city,
                "hospital": hospital_name,  #  Keep the hospital name in response
                "citizen_name": appointment.citizen_name,
                "email": appointment.email,
                "appointment_date": str(appointment.appointment_date)
            }
        }, status=201)
        