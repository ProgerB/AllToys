from django.shortcuts import render
from .models import *
import jprq
from django.utils import timezone


def dashboard(request):
    users = User.objects.all()
    toys = Toy.objects.all()
    toys = toys.filter(created_at__year=timezone.now().year)
    toys = toys.select_related("user")
    toys = toys.prefetch_related("tags")
    return render(request, "dashboard.html", {'toys': toys, 'users': users})


def get_toys(request):
    toys = Toy.objects.all()
    # toys = toys.filter(created_at__year=timezone.now().year)
    toys = toys.select_related("user")
    toys = toys.prefetch_related("tags")
    print(toys)

    return render(request, "toys.html", {"toys": toys})


def get_toy_detail(request, id):
    toy = Toy.objects.get(pk=id)
    return render(request, "toy_detail.html", context={"toy": toy})