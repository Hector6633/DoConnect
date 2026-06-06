from django.urls import path
from . views import *

urlpatterns = [
    path('', dashboard_index, name="dashboard_index"),
    path('appointments/', appointments, name="appointments"),
    path('feedbacks/', feedbacks, name="feedbacks"),
    path('patient-list/', search_patients, name="search_patients"),
]
