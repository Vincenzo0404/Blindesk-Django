# fmt: off
from django.urls import path

from .views import CustomerDelete, CustomerList, CustomerUpdate

# fmt: on

urlpatterns = [
    path("customers/", CustomerList.as_view(), name="customer-list"),
    path(
        "customers/<int:pk>/update/", CustomerUpdate.as_view(), name="customer-update"
    ),
    path(
        "customers/<int:pk>/delete/", CustomerDelete.as_view(), name="customer-delete"
    ),
]
