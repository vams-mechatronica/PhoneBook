from django.shortcuts import render
from .models import *


# Create your views here.
def home(request):
    phonebook = PhoneBookCustomerCare.objects.all()
    context = {'phonebook':phonebook}
    return render(request,"home.html",context)

