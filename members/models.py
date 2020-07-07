from django.db import models
from datetime import datetime


class Member(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    team_role = models.CharField(max_length=25, default='', blank=True)
    num_hours = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    logged_in = models.BooleanField(default=False)
    sign_in_time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        # Ryan Alexander
        return str.capitalize(self.first_name) + " " + str.capitalize(self.last_name)


class Appearance(models.Model):
    date = models.DateField()
    length = models.DecimalField(max_digits=5, decimal_places=2)
    start_time = models.TimeField()
    end_time = models.TimeField()
    member = models.ForeignKey(Member, on_delete=models.CASCADE)

    def __str__(self):
        # Feb 23: 3:05 PM - 5:06 PM
        return self.date.strftime("%b %-d") + ": " + self.start_time.strftime("%-I:%M %p") + " - " + self.end_time.strftime("%-I:%M %p")
