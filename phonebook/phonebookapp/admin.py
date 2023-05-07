from django.contrib import admin
from .models import *
# Register your models here.

class PhoneBookAdmin(admin.ModelAdmin):
    list_display: list = ('companyName','companyLocation','country','contactNo','status')
    ordering: list = ['-status']
    search_fields: list = ('companyName', 'companyLocation',
                           'country', 'contactNo', 'status')


admin.site.register(PhoneBookCustomerCare, PhoneBookAdmin)
