from django.urls import path
from rates.views import get_current_usd

urlpatterns = [
    path('get-current-usd/', get_current_usd, name = 'get_current_usd')
]