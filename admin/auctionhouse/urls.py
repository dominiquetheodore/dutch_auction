from django.urls import path
from . import views

app_name = 'auctionhouse'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:auction_id>/', views.detail, name='detail'),
]