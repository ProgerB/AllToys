from django.shortcuts import render
from .models import *
import jprq


def dashboard(request):
    Users = User.objects.all()
    Toys = Toy.objects.all()
    return render(request, "dashboard.html", {"Users": Users, "Toys": Toys})
