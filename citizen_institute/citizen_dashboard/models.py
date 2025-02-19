from django.db import models

class KhaldaHospitalAppointment(models.Model):
    city = models.CharField(max_length=50, default="Amman")
    hospital = models.CharField(max_length=100, default="Khalda Hospital")
    citizen_name = models.CharField(max_length=100)
    email = models.EmailField()
    appointment_date = models.DateField()

    def __str__(self):
        return f"{self.citizen_name} - {self.appointment_date}"



class BloodDonationAppointment(models.Model):
    BLOOD_TYPES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
    ]
    CHRONIC_DISEASES = [
        ('heart disease', 'Heart Disease'),
        ('diabetic disease', 'Diabetic Disease'),
        ('cancer', 'Cancer'),
        ('asthma', 'Asthma'),
        ('hypertension', 'Hypertension'),
        ('other disease', 'Other Disease'),
        ('no', 'No'),
    ]
    DONATION_UNITS = [
        ('1', '1 Unit'),
        ('2', '2 Units'),
        ('3', '3 Units'),
    ]
    city = models.CharField(max_length=100)
    hospital = models.CharField(max_length=200)
    citizen_name = models.CharField(max_length=255)
    email = models.EmailField()
    blood_type = models.CharField(max_length=3, choices=BLOOD_TYPES)
    chronic_disease = models.CharField(max_length=50, choices=CHRONIC_DISEASES)
    donated_last_two_months = models.BooleanField(default=False)
    donation_units = models.CharField(max_length=1, choices=DONATION_UNITS, null=True, blank=True)
    appointment_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.citizen_name} - {self.blood_type} - {self.hospital} - {self.appointment_date}"