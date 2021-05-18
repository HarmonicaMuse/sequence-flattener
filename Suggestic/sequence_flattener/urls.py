from django.urls import path
from .views import sequence


urlpatterns = [
    path('sequence/', sequence, name="sequence")
]