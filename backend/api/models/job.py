from django.db import models

from .customer import Customer

# from .log_job_stage import LogJobStage


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
    id_customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    city = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    date_estimate_done = models.DateField()
    date_estimate_accepted = models.DateField()
    date_sent_order = models.DateField()
    date_received_cdo = models.DateField()
    date_confirmed_order = models.DateField()
    date_arrived_goods = models.DateField()
    date_closed = models.DateField()

    # def get_stage(self):
    #     return LogJobStage.objects.filter(id_job=self.id).order_by("-started_at")[0]

    def __str__(self):
        return f"Commessa {self.id} - {self.stage}"
