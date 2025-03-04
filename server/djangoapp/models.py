# Uncomment the following imports before adding the Model code

from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    year_made = models.IntegerField()
    def __str__(self):
        return self.name  # Return the name as the string representation


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)  # Many-to-One relationship
    name = models.CharField(max_length=100)
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('COUPE', 'Coupe'),
        ('MINIVAN', 'Minivan'),
        ('HATCHBACK', 'Hatchback'),
        ('CONVERTIBLE', 'Convertible'),
        ('CROSSOVER', 'Crossover'),
        ('SPORTSCARS', 'Sportscar'),  
        ]
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE, related_name='models')
    name = models.CharField(max_length=130)
    type = models.CharField(choices=CAR_TYPES, max_length=15, default="SUV")
    year = models.IntegerField(
        default=2023, validators=[MinValueValidator(2015), MaxValueValidator(2023)]
    )

    def __str__(self):
        return self.name  # Return the name as the string representation
