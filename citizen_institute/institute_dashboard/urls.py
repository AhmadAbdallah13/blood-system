from django.urls import path
from .views import InstituteDashboardView, FilterCitizensView
from .views import DescriptionCaseView


urlpatterns = [
    path('dashboard/', InstituteDashboardView.as_view(), name='institute_dashboard'),
    path("filter_citizens/", FilterCitizensView.as_view(), name="filter_citizens"),
    path('description_case/', DescriptionCaseView.as_view(), name='description_case'),



]
