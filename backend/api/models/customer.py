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

    name = models.CharField(max_length=50)
    surname = models.TextField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    province = models.CharField(max_length=50)
    customer_type = models.CharField(
        max_length=3,
        choices=CUSTOMER_TYPES,
        default=CUSTOMER_TYPES[1],  # B2C
    )
    contact_method = models.CharField(
        max_length=25,
        choices=CONTACT_METHODS,
        default=CONTACT_METHODS[3],  # Passerby
    )
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name="customers"
    )

    def __str__(self):
        return self.name + " " + self.surname
