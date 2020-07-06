from django.db import models
from datetime import datetime


class Member(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    team_role = models.CharField(max_length=25, default='')
    num_hours = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    logged_in = models.BooleanField(default=False)
    sign_in_time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return str.capitalize(self.first_name) + " " + str.capitalize(self.last_name)
