from django.urls import path
from .views import (
    IndexView,
    CitizenSignupView, CitizenSigninView, CitizenDashboardView, CitizenLogoutView,
    InstituteSignupView, InstituteSigninView, InstituteDashboardView, InstituteLogoutView,
    CitizenSignupAPI, CitizenSigninAPI, InstituteSignupAPI, InstituteSigninAPI
)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    
    # Citizen URLs
    path('citizen/signup/', CitizenSignupView.as_view(), name='citizen_signup'),
    path('citizen/signin/', CitizenSigninView.as_view(), name='citizen_signin'),
    path('citizen/dashboard/', CitizenDashboardView.as_view(), name='citizen_dashboard'),
    path('citizen/logout/', CitizenLogoutView.as_view(), name='citizen_logout'),
    
    # Institute URLs
    path('institute/signup/', InstituteSignupView.as_view(), name='institute_signup'),
    path('institute/signin/', InstituteSigninView.as_view(), name='institute_signin'),
    path('institute/dashboard/', InstituteDashboardView.as_view(), name='institute_dashboard'),
    path('institute/logout/', InstituteLogoutView.as_view(), name='institute_logout'),
    
    # API Endpoints
    path('api/citizen/signup/', CitizenSignupAPI.as_view(), name='api_citizen_signup'),
    path('api/citizen/signin/', CitizenSigninAPI.as_view(), name='api_citizen_signin'),
    path('api/institute/signup/', InstituteSignupAPI.as_view(), name='api_institute_signup'),
    path('api/institute/signin/', InstituteSigninAPI.as_view(), name='api_institute_signin'),
]