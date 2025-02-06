from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from .job import Job
from .product import Product


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    q_t = models.IntegerField(validators=[MinValueValidator(1)])
    discount = models.PositiveSmallIntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text="Sconto in percentuale (0-100%)",
    )

    def __str__(self):
        return f"Order {self.id} - {self.product.name}"
