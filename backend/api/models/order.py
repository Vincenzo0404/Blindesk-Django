from django.db import models

from .job import Job
from .product import Product


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    id_job = models.ForeignKey(Job, on_delete=models.CASCADE)
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    q_t = models.IntegerField()
    discount = models.FloatField(default=0.0)

    def __str__(self):
        return f"Order {self.id} - {self.id_product.name}"
