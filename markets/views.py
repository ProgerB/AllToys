from django.shortcuts import render
from .models import Markets
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


# def index(request):
#     markets = Markets.objects.all()
#     return render(request, "index.html", context={"markets": markets})


# def get_market_detail(request, id):
#     market = Markets.objects.get(pk=id)
#     return render(request, "market_detail.html", context={"market": market})


class HomeView(ListView):
    model = Markets
    template_name = 'index.html'


class MarketDetailView(DetailView):
    model = Markets
    template_name = "market_detail.html"

    def get_context_data(self, *args, **kwargs):
        markets = Markets.objects.all()
        # market = Markets.objects.get(pk=id)
        context = super(MarketDetailView, self).get_context_data(*args, **kwargs)
        context["markets"] = markets
        return context
