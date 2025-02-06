from django.db import models

from .category import Category
from .supplier import Supplier


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["name", "category"], name="unique_product_name_category"
            )
        ]

    def __str__(self):
        return self.name
