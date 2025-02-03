from django.urls import path

from . import views

urlpatterns = [
    path("customers/", views.CustomerList.as_view(), name="customer_list"),
]
