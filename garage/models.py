import datetime
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Car(models.Model):
    CHOICES = [('Petrol', 'Petrol'), ('Diesel', 'Diesel'), ('Petrol / LPG', 'Petrol / LPG'),
               ('Hybrid', 'Hybrid'), ('Electrical', 'Electrical')]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    fuel = models.CharField(max_length=50, choices=CHOICES)
    color = models.CharField(max_length=50, default='')
    date_of_production = models.CharField(max_length=50, default='')
    image = models.ImageField(default='no_image.png', upload_to='users_cars_pics')
    created = models.DateTimeField(default=datetime.datetime.now())

    class Meta:
        ordering = ['make', ]

    def __str__(self):
        return self.make

    def get_absolute_url(self):
        return reverse('car-detail', kwargs={'pk': self.pk})

