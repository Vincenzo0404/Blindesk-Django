from django.db import models

from .customer import Customer


class Job(models.Model):

    STAGES = [
        ("estimate done", "Estimate"),
        ("estimate_accepted", "Estimate accepted"),
        ("sent_order", "Sent order"),
        ("received_cdo", "Received CDO"),
        ("confirmed_order", "Confirmed order"),
        ("arrived_goods", "Arrived goods"),
        ("closed", "Closed"),
    ]

    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    city = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    stage = models.CharField(max_length=255, choices=STAGES, default=STAGES[0][0])

    def __str__(self):
        return f"Commessa {self.id} - {self.stage}"
