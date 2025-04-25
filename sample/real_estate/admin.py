from django.contrib import admin
from real_estate.models import Apartment
# Register your models here.

class ApartmentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Apartment, ApartmentAdmin)