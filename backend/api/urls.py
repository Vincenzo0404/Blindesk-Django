# fmt: off
from django.urls import path

from .views import *

# fmt: on

urlpatterns = [
    # Customers
    path("customer/list/", CustomerList.as_view(), name="customer-list"),
    path("customer/update/<int:pk>/", CustomerUpdate.as_view(), name="customer-update"),
    path("customer/delete/<int:pk>/", CustomerDelete.as_view(), name="customer-delete"),
    path("customer/create/", CustomerCreate.as_view(), name="customer-create"),
    # Jobs
    path("job/list/", JobList.as_view(), name="job-list"),
    path("job/create/", JobCreate.as_view(), name="job-create"),
    path("job/update/<int:pk>/", JobUpdate.as_view(), name="job-update"),
    path("job/delete/<int:pk>/", JobDelete.as_view(), name="job-delete"),
    path("job/stage-choices/", JobStageChoices.as_view(), name="job-stage-choices"),
]
