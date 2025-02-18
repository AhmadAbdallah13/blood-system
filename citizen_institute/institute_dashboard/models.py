from django.db import models
# Create your models here.



class UrgentCaseList(models.Model):
    type_case = models.CharField(max_length=200)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
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
    address = models.CharField(max_length=20)  
    
    def __str__(self):
        return f"{self.type_case} - {self.first_name} {self.last_name}"