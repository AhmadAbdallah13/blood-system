from django.db import models
from django.contrib.auth.hashers import make_password

class Citizen(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    national_id = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True, null=False, blank=False)


    BLOOD_TYPES = [
        ("A+", "A+"),
        ("A-", "A-"),
        ("B+", "B+"),
        ("B-", "B-"),
        ("AB+", "AB+"),
        ("AB-", "AB-"),
        ("O+", "O+"),
        ("O-", "O-"),
    ]

    blood_type = models.CharField(max_length=3, choices=BLOOD_TYPES)
    CITIES = [
        ("Amman", "Amman"),
        ("Irbid", "Irbid"),
        ("Aqaba", "Aqaba"),
    ]

    ADDRESSES = {
        "Amman": [("Shmesani", "Shmesani"), ("Khalda", "Khalda"), ("Makka Street", "Makka Street")],
        "Irbid": [("Downtown Irbid", "Downtown Irbid"), ("West", "West"), ("East", "East")],
        "Aqaba": [("Downtown Aqaba", "Downtown Aqaba"), ("Beach Street", "Beach Street")],
    }

    city = models.CharField(max_length=10, choices=CITIES)
    address = models.CharField(max_length=20)  # No choices because it depends on city
    password = models.CharField(max_length=255)


    def save(self, *args, **kwargs):
        if not self.password.startswith('pbkdf2_sha256$'):  # Prevent double hashing
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

class Institute(models.Model):
    name = models.CharField(max_length=255, unique=True)
    institute_type = models.CharField(max_length=50, choices=[('Hospital', 'Hospital'), ('Blood Bank', 'Blood Bank'), ('Clinic', 'Clinic')])
    phone_number = models.CharField(max_length=15, unique=True, null=True, blank=True)
    email = models.EmailField(unique=True)
    city = models.CharField(max_length=100, choices=[('Shmesani', 'Shmesani'), ('Khalda', 'Khalda'), ('Makka Street', 'Makka Street')])
    address = models.CharField(max_length=100)
    password = models.CharField(max_length=255)



    def save(self, *args, **kwargs):
        if not self.password.startswith('pbkdf2_sha256$'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)
