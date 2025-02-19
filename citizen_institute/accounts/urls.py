from django.urls import path 
from .views import CitizenDashboardView
from .views import InstituteDashboardView
from .views import IndexView
from .views import (
    IndexView,  # Add index view
    CitizenSignupView, CitizenSigninView, InstituteSignupView, InstituteSigninView, 
    CitizenSignupAPI, CitizenSigninAPI, InstituteSignupAPI, InstituteSigninAPI
)

urlpatterns = [
    # Index page
    path('', IndexView.as_view(), name='index'),  # Add this line

    # Template-based views
    path('citizen/signup/', CitizenSignupView.as_view(), name='citizen_signup'),
    path('citizen/signin/', CitizenSigninView.as_view(), name='citizen_signin'),
    path('institute/signup/', InstituteSignupView.as_view(), name='institute_signup'),
    path('institute/signin/', InstituteSigninView.as_view(), name='institute_signin'),
    path('dashboard/', CitizenDashboardView.as_view(), name='dashboard'),
    path('dashboard/', InstituteDashboardView.as_view(), name='dashboard'),


    # API endpoints (kept for reference)
    path('api/citizen/signup/', CitizenSignupAPI.as_view(), name='api_citizen_signup'),
    path('api/citizen/signin/', CitizenSigninAPI.as_view(), name='api_citizen_signin'),
    path('api/institute/signup/', InstituteSignupAPI.as_view(), name='api_institute_signup'),
    path('api/institute/signin/', InstituteSigninAPI.as_view(), name='api_institute_signin'),
]
