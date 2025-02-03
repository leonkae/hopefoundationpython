from django.urls import path

from .views import *
from . import views

urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    path('donate/',views.DonateView.as_view(),name="donate")
]
