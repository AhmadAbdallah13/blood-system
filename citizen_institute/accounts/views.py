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
from django.utils.decorators import method_decorator
from .forms import CitizenSignupForm 
from django.views.generic.edit import FormView
from .forms import InstituteSignupForm
from django.urls import reverse_lazy




# Custom decorators for auth checks
def citizen_login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.session.get('citizen_id'):
            messages.error(request, "Please login first!")
            return redirect('citizen_signin')
        return view_func(request, *args, **kwargs)
    return wrapper

def institute_login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.session.get('institute_id'):
            messages.error(request, "Please login first!")
            return redirect('institute_signin')
        return view_func(request, *args, **kwargs)
    return wrapper

### TEMPLATE-BASED VIEWS ###

class IndexView(TemplateView):
    template_name = "index.html"

class CitizenSignupView(FormView):
    template_name = 'accounts/citizen_signup.html'
    form_class = CitizenSignupForm
    success_url = '/citizen/signin/'  # Adjust as needed

    def form_valid(self, form):
        # Save the citizen to the database
        Citizen.objects.create(
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
            national_id=form.cleaned_data['national_id'],
            email=form.cleaned_data['email'],
            phone_number=form.cleaned_data['phone_number'] or None,
            blood_type=form.cleaned_data['blood_type'],
            city=form.cleaned_data['city'],
            address=form.cleaned_data['address'],
            password=make_password(form.cleaned_data['password']),
        )
        messages.success(self.request, "Account created successfully! Please sign in.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Please correct the errors below.")
        return self.render_to_response(self.get_context_data(form=form))

class CitizenSigninView(View):
    def get(self, request):
        return render(request, 'accounts/citizen_signin.html')
    
    def post(self, request):
        email = request.POST.get('email')  # Changed to get()
        password = request.POST.get('password')
        
        if not email or not password:  # Added validation
            messages.error(request, "Please fill in all fields")
            return redirect('citizen_signin')

        try:
            citizen = Citizen.objects.get(email=email)
            if check_password(password, citizen.password):
                request.session['citizen_id'] = citizen.id
                request.session['citizen_email'] = citizen.email
                request.session['first_name'] = citizen.first_name
                request.session['last_name'] = citizen.last_name
                request.session.save()  # Force session save
                messages.success(request, "Login successful!")
                return redirect('citizen_dashboard')
            messages.error(request, "Invalid credentials!")
        except Citizen.DoesNotExist:
            messages.error(request, "User not found!")
        return redirect('citizen_signin')

@method_decorator(citizen_login_required, name='dispatch')
class CitizenDashboardView(View):
    def get(self, request):
        try:
            citizen = Citizen.objects.get(id=request.session['citizen_id'])
            return render(request, 'citizen_dashboard/cdashboard.html', {
                'first_name': citizen.first_name,
                'last_name': citizen.last_name
            })
        except Citizen.DoesNotExist:
            messages.error(request, "Session expired!")
            return redirect('citizen_signin')

class CitizenLogoutView(View):
    def get(self, request):
        request.session.flush()  # Complete session cleanup
        messages.success(request, "Logged out successfully!")
        return redirect('citizen_signin')

class InstituteSignupView(FormView):
    template_name = 'accounts/institute_signup.html'
    form_class = InstituteSignupForm
    success_url = reverse_lazy('institute_signin')

    def form_valid(self, form):
        # Check if passwords match
        password = form.cleaned_data['password']
        confirm_password = form.cleaned_data['confirm_password']
        if password != confirm_password:
            messages.error(self.request, "Passwords do not match!")
            return redirect('institute_signup')

        # Check for duplicate entries
        if (Institute.objects.filter(name=form.cleaned_data['name']).exists() or
            Institute.objects.filter(email=form.cleaned_data['email']).exists() or
            Institute.objects.filter(phone_number=form.cleaned_data['phone_number']).exists()):
            messages.error(self.request, "Institute name, email, or phone number already exists!")
            return redirect('institute_signup')

        # Create institute
        Institute.objects.create(
            name=form.cleaned_data['name'],
            institute_type=form.cleaned_data['institute_type'],
            phone_number=form.cleaned_data['phone_number'] or None,
            email=form.cleaned_data['email'],
            city=form.cleaned_data['city'],
            address=form.cleaned_data['address'],
            password=make_password(password)
        )
        messages.success(self.request, "Account created successfully! Please sign in.")
        return super().form_valid(form)

class InstituteSigninView(View):
    def get(self, request):
        return render(request, 'accounts/institute_signin.html')
    
    def post(self, request):
        email = request.POST.get('email')  # Changed to get()
        password = request.POST.get('password')
        
        if not email or not password:  # Added validation
            messages.error(request, "Please fill in all fields")
            return redirect('institute_signin')

        try:
            institute = Institute.objects.get(email=email)
            if check_password(password, institute.password):
                request.session['institute_id'] = institute.id
                request.session['institute_email'] = institute.email
                request.session['name'] = institute.name
                request.session.save()  # Force session save
                messages.success(request, "Login successful!")
                return redirect('institute_dashboard')
            messages.error(request, "Invalid credentials!")
        except Institute.DoesNotExist:
            messages.error(request, "Institute not found!")
        return redirect('institute_signin')

@method_decorator(institute_login_required, name='dispatch')
class InstituteDashboardView(View):
    def get(self, request):
        try:
            institute = Institute.objects.get(id=request.session['institute_id'])
            return render(request, 'institute_dashboard/dashboard.html', {
                'name': institute.name
            })
        except Institute.DoesNotExist:
            messages.error(request, "Session expired!")
            return redirect('institute_signin')

class InstituteLogoutView(View):
    def get(self, request):
        request.session.flush()  # Complete session cleanup
        messages.success(request, "Logged out successfully!")
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
        
        
        
#-------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
        
        # Citizen APIs

class CitizenSignupAPI(APIView):
    def post(self, request):
        data = request.data
        if data['password'] != data['confirm_password']:
            return Response({"error": "Passwords do not match!"}, status=status.HTTP_400_BAD_REQUEST)
        
        if Citizen.objects.filter(national_id=data['national_id']).exists() or \
           Citizen.objects.filter(email=data['email']).exists() or \
           Citizen.objects.filter(phone_number=data['phone_number']).exists():
            return Response({"error": "National ID, Email, or Phone number already exists!"}, status=status.HTTP_400_BAD_REQUEST)
        
        data['password'] = make_password(data['password'])
        citizen = Citizen.objects.create(**data)
        return Response(CitizenSerializer(citizen).data, status=status.HTTP_201_CREATED)

class CitizenSigninAPI(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        citizen = get_object_or_404(Citizen, email=email)
        
        if check_password(password, citizen.password):
            request.session['citizen_id'] = citizen.id
            request.session['citizen_email'] = citizen.email
            return Response({"message": "Login successful!"}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid credentials!"}, status=status.HTTP_400_BAD_REQUEST)

class CitizenDashboardAPI(APIView):
    @citizen_login_required
    def get(self, request):
        citizen = get_object_or_404(Citizen, id=request.session['citizen_id'])
        return Response(CitizenSerializer(citizen).data, status=status.HTTP_200_OK)

class CitizenLogoutAPI(APIView):
    def post(self, request):
        request.session.flush()
        return Response({"message": "Logged out successfully!"}, status=status.HTTP_200_OK)

# Institute APIs

class InstituteSignupAPI(APIView):
    def post(self, request):
        data = request.data
        if data['password'] != data['confirm_password']:
            return Response({"error": "Passwords do not match!"}, status=status.HTTP_400_BAD_REQUEST)
        
        if Institute.objects.filter(name=data['name']).exists() or \
           Institute.objects.filter(email=data['email']).exists() or \
           Institute.objects.filter(phone_number=data['phone_number']).exists():
            return Response({"error": "Institute name, email, or phone number already exists!"}, status=status.HTTP_400_BAD_REQUEST)
        
        data['password'] = make_password(data['password'])
        institute = Institute.objects.create(**data)
        return Response(InstituteSerializer(institute).data, status=status.HTTP_201_CREATED)

class InstituteSigninAPI(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        institute = get_object_or_404(Institute, email=email)
        
        if check_password(password, institute.password):
            request.session['institute_id'] = institute.id
            request.session['institute_email'] = institute.email
            return Response({"message": "Login successful!"}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid credentials!"}, status=status.HTTP_400_BAD_REQUEST)

class InstituteDashboardAPI(APIView):
    @institute_login_required
    def get(self, request):
        institute = get_object_or_404(Institute, id=request.session['institute_id'])
        return Response(InstituteSerializer(institute).data, status=status.HTTP_200_OK)

class InstituteLogoutAPI(APIView):
    def post(self, request):
        request.session.flush()
        return Response({"message": "Logged out successfully!"}, status=status.HTTP_200_OK)