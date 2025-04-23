from django.contrib import admin
from django.urls import path, include
from payment import views


app_name = "payment"

urlpatterns = [
    path("process/",views.payment_process,name="payment_process")
]



