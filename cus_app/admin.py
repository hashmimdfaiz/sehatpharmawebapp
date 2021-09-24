from django.contrib import admin
from .models import Customer


# Register your models here.
class Customers_details(admin.ModelAdmin):
    list_display = ['customer_id', 'name', 'phone_no', 'email_id','area']


admin.site.register(Customer, Customers_details)
