from django.contrib.auth.models import User
from rest_framework import serializers

from .models.category import Category
from .models.customer import Customer
from .models.feature import Feature
from .models.job import Job
from .models.job_stage import JobStage
from .models.log_job_stage import LogJobStage
from .models.monetization import Monetization
from .models.order import Order
from .models.order_detail import OrderDetail
from .models.product import Product
from .models.product_feature import ProductFeature
from .models.supplier import Supplier


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        return user


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = "__all__"


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = "__all__"


class JobStageSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobStage
        fields = "__all__"


class LogJobStageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogJobStage
        fields = "__all__"


class MonetizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monetization
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ProductFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductFeature
        fields = "__all__"


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = "__all__"
