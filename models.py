# This file does not need to be changed
from django.db import models


class AppointmentRequest:
    def __init__(self, stylist_name, start_datetime, session_length=30):
        self.stylist_name = stylist_name
        self.start_datetime = start_datetime
        self.session_length = session_length


SPECIALITY_CHOICES = [("cut", "Haircuts"), ("dye", "Hair Dying"), ("shave", "Shaving")]


class Stylist(models.Model):
    name = models.TextField()
    speciality = models.CharField(max_length=5, choices=SPECIALITY_CHOICES)
    accepting_new_clients = models.BooleanField(default=False)
