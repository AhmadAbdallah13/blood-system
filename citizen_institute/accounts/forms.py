from django import forms
from .models import Citizen

class CitizenSignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Citizen
        fields = ['first_name', 'last_name', 'national_id', 'email', 'phone_number', 
                  'blood_type', 'city', 'address', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error("confirm_password", "Passwords do not match!")

        if Citizen.objects.filter(national_id=cleaned_data.get("national_id")).exists():
            self.add_error("national_id", "National ID already exists!")

        if Citizen.objects.filter(email=cleaned_data.get("email")).exists():
            self.add_error("email", "Email already exists!")

        if Citizen.objects.filter(phone_number=cleaned_data.get("phone_number")).exists():
            self.add_error("phone_number", "Phone number already exists!")
            

class InstituteSignupForm(forms.Form):
    name = forms.CharField(max_length=255)
    institute_type = forms.CharField(max_length=255)
    phone_number = forms.CharField(max_length=20, required=False)
    email = forms.EmailField()
    city = forms.CharField(max_length=255)
    address = forms.CharField(widget=forms.Textarea)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)