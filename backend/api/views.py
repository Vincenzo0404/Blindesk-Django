from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .forms import *
from .models import *
from .serializers import *


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
