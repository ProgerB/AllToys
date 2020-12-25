from django.urls import path
from markets import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='market_list'),
    path('market/<int:pk>/', views.MarketDetailView.as_view(), name='market_detail'),
]
