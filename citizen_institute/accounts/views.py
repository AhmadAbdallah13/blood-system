from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Citizen, Institute
from .serializers import CitizenSerializer, InstituteSerializer
from django.views import View
from django.views.generic import TemplateView
from django.http import JsonResponse




### TEMPLATE-BASED VIEWS ###

class IndexView(TemplateView):
    template_name = "index.html"

class CitizenSignupView(View):
    def get(self, request):
        return render(request, 'accounts/citizen_signup.html')
    
    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        national_id = request.POST.get('national_id')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        blood_type = request.POST.get('blood_type')
        city = request.POST.get('city')
        address = request.POST.get('address')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('citizen_signup')

        if Citizen.objects.filter(national_id=national_id).exists() or \
           Citizen.objects.filter(email=email).exists() or \
           Citizen.objects.filter(phone_number=phone_number).exists():
            messages.error(request, "National ID, Email, or Phone number already exists!")
            return redirect('citizen_signup')

        Citizen.objects.create(
            first_name=first_name,
            last_name=last_name,
            national_id=national_id,
            email=email,
            phone_number=phone_number or None,
            blood_type=blood_type,
            city=city,
            address=address,
            password=make_password(password)
        )
        messages.success(request, "Account created successfully! Please sign in.")
        return redirect('citizen_signin')

class CitizenSigninView(View):
    def get(self, request):
        return render(request, 'accounts/citizen_signin.html')
    
    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        
        try:
            citizen = Citizen.objects.get(email=email)
            if check_password(password, citizen.password):
                messages.success(request, "Login successful!")
                return redirect('dashboard')
            else:
                messages.error(request, "Invalid credentials!")
        except Citizen.DoesNotExist:
            messages.error(request, "User not found!")
        return redirect('citizen_signin')

class InstituteSignupView(View):
    def get(self, request):
        return render(request, 'accounts/institute_signup.html')
    
    def post(self, request):
        name = request.POST['name']
        institute_type = request.POST['institute_type']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        city = request.POST['city']
        address = request.POST['address']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('institute_signup')
        
        Institute.objects.create(
            name=name,
            institute_type=institute_type,
            phone_number=phone_number,
            email=email,
            city=city,
            address=address,
            password=make_password(password)
        )
        messages.success(request, "Account created successfully! Please sign in.")
        return redirect('institute_signin')

class InstituteSigninView(View):
    def get(self, request):
        return render(request, 'accounts/institute_signin.html')
    
    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        
        try:
            institute = Institute.objects.get(email=email)
            if check_password(password, institute.password):
                messages.success(request, "Login successful!")
                return redirect('institute_dashboard')
            else:
                messages.error(request, "Invalid credentials!")
        except Institute.DoesNotExist:
            messages.error(request, "User not found!")
        return redirect('institute_signin')

### REST API VIEWS ###



class CitizenSignupAPI(APIView):
    def post(self, request):
        serializer = CitizenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['password'] = make_password(serializer.validated_data['password'])  
            citizen = serializer.save()
            return JsonResponse({
                "message": "Citizen created successfully!",
                "citizen": CitizenSerializer(citizen).data
            }, status=status.HTTP_201_CREATED, safe=False)
        return JsonResponse({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST, safe=False)


class CitizenSigninAPI(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            citizen = Citizen.objects.get(email=email)
            if check_password(password, citizen.password):
                return JsonResponse({
                    "message": "Login successful!",
                    "citizen": CitizenSerializer(citizen).data
                }, status=status.HTTP_200_OK, safe=False)
            else:
                return JsonResponse({"error": "Invalid credentials!"}, status=status.HTTP_401_UNAUTHORIZED, safe=False)
        except Citizen.DoesNotExist:
            return JsonResponse({"error": "User not found!"}, status=status.HTTP_404_NOT_FOUND, safe=False)


class InstituteSignupAPI(APIView):
    def post(self, request):
        serializer = InstituteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['password'] = make_password(serializer.validated_data['password'])  
            institute = serializer.save()
            return JsonResponse({
                "message": "Institute created successfully!",
                "institute": InstituteSerializer(institute).data
            }, status=status.HTTP_201_CREATED, safe=False)
        return JsonResponse({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST, safe=False)


class InstituteSigninAPI(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            institute = Institute.objects.get(email=email)
            if check_password(password, institute.password):
                return JsonResponse({
                    "message": "Login successful!",
                    "institute": InstituteSerializer(institute).data
                }, status=status.HTTP_200_OK, safe=False)
            else:
                return JsonResponse({"error": "Invalid credentials!"}, status=status.HTTP_401_UNAUTHORIZED, safe=False)
        except Institute.DoesNotExist:
            return JsonResponse({"error": "User not found!"}, status=status.HTTP_404_NOT_FOUND, safe=False)