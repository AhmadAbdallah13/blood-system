from django.db import models

class KhaldaHospitalAppointment(models.Model):
    city = models.CharField(max_length=50, default="Amman")
    hospital = models.CharField(max_length=100, default="Khalda Hospital")
    citizen_name = models.CharField(max_length=100)
    email = models.EmailField()
    appointment_date = models.DateField()

    def __str__(self):
        return f"{self.citizen_name} - {self.appointment_date}"
