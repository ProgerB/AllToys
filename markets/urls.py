from django.urls import path
from markets import views

urlpatterns = [
    path('', views.index, name='index'),
    path('market/<int:id>/', views.get_market_detail, name='market_detail'),
]
