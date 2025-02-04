from django.db import models

from .category import Category
from .supplier import Supplier


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    id_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    id_supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
