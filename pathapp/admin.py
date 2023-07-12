from django.contrib import admin
from .models import Patient, Test, Payment, Report
# Register your models here.
admin.site.register(Patient)
admin.site.register(Test)
admin.site.register(Payment)
admin.site.register(Report)