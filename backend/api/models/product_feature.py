from django.db import models

from .feature import Feature
from .product import Product


class ProductFeature(models.Model):
    id = models.AutoField(primary_key=True)
    id_feature = models.ForeignKey(Feature, on_delete=models.CASCADE)
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    value = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.id_product.name} - {self.id_feature.name}: {self.value}"
