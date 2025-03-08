# fmt: off
from django.urls import path

from .views import *

# fmt: on

urlpatterns = [
    # generic views for the API
    path(
        "model-metadata/<str:model_name>/",
        ModelMetadata.as_view(),
        name="model-metadata",
    ),
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
    # Categories
    path("category/list/", CategoryList.as_view(), name="category-list"),
    path("category/create/", CategoryCreate.as_view(), name="category-create"),
    path("category/update/<int:pk>/", CategoryUpdate.as_view(), name="category-update"),
    # Features
    path("feature/list/", FeatureList.as_view(), name="feature-list"),
    path("feature/create/", FeatureCreate.as_view(), name="feature-create"),
    path("feature/update/<int:pk>/", FeatureUpdate.as_view(), name="feature-update"),
    # Products
    path("product/list/", ProductList.as_view(), name="product-list"),
    path("product/create/", ProductCreate.as_view(), name="product-create"),
    path("product/update/<int:pk>/", ProductUpdate.as_view(), name="product-update"),
    # product features
    path(
        "productfeature/list/",
        ProductFeatureList.as_view(),
        name="product-feature-list",
    ),
    path(
        "productfeature/create/",
        ProductFeatureCreate.as_view(),
        name="product-feature-create",
    ),
    path(
        "productfeature/update/<int:pk>/",
        ProductFeatureUpdate.as_view(),
        name="product-feature-update",
    ),
    # Suppliers
    path("supplier/list/", SupplierList.as_view(), name="supplier-list"),
    path("supplier/create/", SupplierCreate.as_view(), name="supplier-create"),
]
