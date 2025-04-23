from django.urls import path
from orders import views

app_name = "orders"

urlpatterns = [
    path("create/", views.create_orders, name="create_orders")
]

