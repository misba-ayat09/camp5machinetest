from django.db import models


class Flight(models.Model):
    # Unique identifier for the flight
    flight_id = models.CharField(max_length=10, unique=True)
    dep_airport = models.CharField(max_length=100)  # Departure airport
    dep_date = models.DateField()  # Departure date
    dep_time = models.TimeField()  # Departure time
    arr_airport = models.CharField(max_length=100)  # Arrival airport
    arr_date = models.DateField()  # Arrival date
    arr_time = models.TimeField()  # Arrival time

    def __str__(self):
        return f"{self.flight_id} - {self.dep_airport} to {self.arr_airport}"
