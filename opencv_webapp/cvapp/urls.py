from django.urls import path
from .views import *

urlpatterns = [
    path('', first_view, name="first_view"),
]
