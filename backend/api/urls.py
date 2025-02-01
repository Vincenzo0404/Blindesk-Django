from django.urls import path

from . import views

urlpatterns = [
    path("customers/", views.CustomerList.as_view(), name="customer_list"),
    # path("customers/<int:pk>/", views.CustomerDetail.as_view(), name="customer_detail"),
    # path("customers/create/", views.CustomerCreate.as_view(), name="customer_create"),
    # path(
    #     "customers/update/<int:pk>/",
    #     views.CustomerUpdate.as_view(),
    #     name="customer_update",
    # ),
    # path(
    #     "customers/delete/<int:pk>/",
    #     views.CustomerDelete.as_view(),
    #     name="customer_delete",
    # ),
]
