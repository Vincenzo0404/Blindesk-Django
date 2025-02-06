from django.db import models

from .feature import Feature
from .product import Product


class ProductFeature(models.Model):
    id = models.AutoField(primary_key=True)
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    value = models.CharField(max_length=255)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["feature", "product"], name="unique_product_feature"
            )
        ]

    def __str__(self):
        return f"{self.product.name} - {self.feature.name}: {self.value}"
