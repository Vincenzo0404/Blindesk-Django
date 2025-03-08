from django.db import models

from .category import Category
from .supplier import Supplier


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    unit_cost = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
    )
    unit_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    features = models.ManyToManyField(
        "api.Feature", through="api.ProductFeature", related_name="products"
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["name", "category"], name="unique_product_name_category"
            )
        ]

    def __str__(self):
        return self.name
