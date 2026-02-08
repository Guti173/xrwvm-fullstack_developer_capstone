from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class CarMake(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    country = models.CharField(max_length=60, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class CarModel(models.Model):
    # Many-to-one relationship: one make can have many models
    car_make = models.ForeignKey(
        CarMake, on_delete=models.CASCADE, related_name="models"
    )

    # Dealer ID (from Cloudant/Dealerships service)
    dealer_id = models.IntegerField()

    name = models.CharField(max_length=100)

    CAR_TYPES = [
        ("SEDAN", "Sedan"),
        ("SUV", "SUV"),
        ("WAGON", "Wagon"),
        ("TRUCK", "Truck"),
        ("COUPE", "Coupe"),
        ("HATCHBACK", "Hatchback"),
        ("CONVERTIBLE", "Convertible"),
        ("VAN", "Van"),
    ]

    type = models.CharField(max_length=12, choices=CAR_TYPES, default="SUV")

    year = models.IntegerField(
        default=2023,
        validators=[
            MinValueValidator(2015),
            MaxValueValidator(2023),
        ],
    )

    # Extra field
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.car_make.name} {self.name} ({self.year})"
