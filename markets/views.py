from django.shortcuts import render
from .models import Markets


def index(request):
    markets = Markets.objects.all()
    return render(request, "index.html", context={"markets": markets})


def get_market_detail(request, id):
    market = Markets.objects.get(pk=id)
    return render(request, "market_detail.html", context={"market": market})