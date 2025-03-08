from django.apps import apps
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .forms import *
from .models import *
from .serializers import *


# generic views for the API
class ModelMetadata(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, model_name):
        # Sostituisci 'api' con il nome effettivo della tua applicazione
        app_name = "api"
        model = apps.get_model(app_name, model_name)
        if not model:
            return Response({"error": "Model not found"}, status=404)

        fields = []
        for field in model._meta.get_fields():
            # Escludi i campi relazionali che non sono ForeignKey
            if field.is_relation and not field.many_to_one and not field.one_to_one:
                continue

            field_info = {
                "name": field.name,
                "type": field.get_internal_type(),
                "choices": field.choices if hasattr(field, "choices") else None,
            }

            # Se il campo è una ForeignKey, aggiungi i possibili record come scelte
            if field.get_internal_type() == "ForeignKey":
                related_model = field.related_model
                related_objects = related_model.objects.all()
                field_info["type"] = "singleSelect"
                field_info["choices"] = [
                    {"id": obj.id, "display": str(obj)} for obj in related_objects
                ]

            fields.append(field_info)

        return Response(fields)


# Customers
class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]


class CustomerUpdate(generics.RetrieveUpdateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]


class CustomerCreate(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]


class CustomerDelete(generics.DestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]


# Jobs
class JobList(generics.ListCreateAPIView):

    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]


class JobCreate(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        form = JobForm(request.data)
        if form.is_valid():
            form.save()
            return Response({"success": True}, status=status.HTTP_201_CREATED)
        return Response(
            {"success": False, "errors": form.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )


class JobUpdate(generics.RetrieveUpdateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]


class JobDelete(generics.DestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]


class JobStageChoices(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        choices = Job.STAGES
        data = [{"value": choice[0], "label": choice[1]} for choice in choices]
        return Response(data)


# Categories
class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]


class CategoryCreate(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]


class CategoryUpdate(generics.RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]


# Features
class FeatureList(generics.ListCreateAPIView):
    serializer_class = FeatureSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        category_id = self.request.query_params.get("category", None)
        if category_id is not None:
            return Feature.objects.filter(category_id=category_id)
        return


class FeatureCreate(generics.CreateAPIView):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer
    permission_classes = [IsAuthenticated]


class FeatureUpdate(generics.RetrieveUpdateAPIView):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer
    permission_classes = [IsAuthenticated]


# Products
class ProductList(generics.ListCreateAPIView):

    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        category_id = self.request.query_params.get("category", None)
        if category_id is not None:
            return Product.objects.filter(category_id=category_id)
        return Product.objects.all()


class ProductCreate(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


class ProductUpdate(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


# Product Features
class ProductFeatureList(generics.ListCreateAPIView):

    serializer_class = ProductFeatureSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        product_id = self.request.query_params.get("product", None)
        if product_id is not None:
            return ProductFeature.objects.filter(product_id=product_id)
        return ProductFeature.objects.all()


class ProductFeatureCreate(generics.CreateAPIView):
    queryset = ProductFeature.objects.all()
    serializer_class = ProductFeatureSerializer
    permission_classes = [IsAuthenticated]


class ProductFeatureUpdate(generics.RetrieveUpdateAPIView):
    queryset = ProductFeature.objects.all()
    serializer_class = ProductFeatureSerializer
    permission_classes = [IsAuthenticated]


# Suppliers
class SupplierList(generics.ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [IsAuthenticated]


class SupplierCreate(generics.CreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [IsAuthenticated]
