from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.generic import TemplateView
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from accounts.models import Citizen
from .serializers import CitizenSerializer
import json
from .models import UrgentCaseList


class InstituteDashboardView(TemplateView):
    template_name = "institute_dashboard/dashboard.html"
    
    
class DescriptionCaseView(TemplateView):
    template_name = "institute_dashboard/description_case.html"

    def get(self, request):
        return self.render_to_response({})

    def post(self, request):
        # Get form data
        type_case = request.POST.get("type_case")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        blood_type = request.POST.get("blood_type")
        city = request.POST.get("city")
        address = request.POST.get("address")

        # Validate data
        if not all([type_case, first_name, last_name, blood_type, city, address]):
            return JsonResponse({"success": False, "message": "All fields are required"}, status=400)

        # Save data in the database
        urgent_case = UrgentCaseList.objects.create(
            type_case=type_case,
            first_name=first_name,
            last_name=last_name,
            blood_type=blood_type,
            city=city,
            address=address
        )

        return JsonResponse({
            "success": True,
            "message": "Case added successfully",
            "case_id": urgent_case.id
        })


@method_decorator(csrf_exempt, name='dispatch')  # Disable CSRF for testing (not recommended in production)
class FilterCitizensView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            city = data.get("city", "").strip()
            address = data.get("address", "").strip()
            blood_type = data.get("blood_type", "").strip()

            # Use Django ORM to filter the Citizen model
            citizens = Citizen.objects.filter(
                city__icontains=city, 
                address__icontains=address, 
                blood_type=blood_type
            ).values("first_name", "last_name", "city", "address", "blood_type", "phone_number")

            return JsonResponse(list(citizens), safe=False)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    def get(self, request, *args, **kwargs):
        return JsonResponse({"successful": "valid !"}, status=400)
