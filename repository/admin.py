from django.contrib import admin
from repository import models

# Register your models here.

admin.site.register(models.Cinema)
admin.site.register(models.Movie)
admin.site.register(models.Plan)
admin.site.register(models.Seat)
admin.site.register(models.Ticket)
