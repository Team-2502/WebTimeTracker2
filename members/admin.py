from django.contrib import admin

from .models import Member
from .models import Appearance

admin.site.register(Member)
admin.site.register(Appearance)
