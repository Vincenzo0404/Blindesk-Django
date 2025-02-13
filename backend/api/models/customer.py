from django.contrib.auth.models import User
from django.db import models


class Customer(models.Model):
    CUSTOMER_TYPES = [("B2B", "Rivenditore"), ("B2C", "privato")]
    CONTACT_METHODS = [
        ("facebook", "Facebook"),
        ("website", "Sito Web"),
        ("word-of-mouth", "Passaparola"),
        ("passerby", "Passante"),
    ]

    name = models.CharField(max_length=50, default="New")
    surname = models.TextField(max_length=50, default="Customer")
    created_at = models.DateTimeField(auto_now_add=True)
    province = models.CharField(max_length=50, default="AQ")
    customer_type = models.CharField(
        max_length=25,
        choices=CUSTOMER_TYPES,
        default=CUSTOMER_TYPES[1][0],  # B2C
    )
    contact_method = models.CharField(
        max_length=25,
        choices=CONTACT_METHODS,
        default=CONTACT_METHODS[3][0],  # Passerby
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="customers",
        default=1,
    )

    def __str__(self):
        return self.name + " " + self.surname
