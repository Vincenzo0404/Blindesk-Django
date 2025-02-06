from django.db import models

from .customer import Customer


class Job(models.Model):

    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    city = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    # def get_stage(self):
    #     return LogJobStage.objects.filter(id_job=self.id).order_by("-started_at")[0]

    def __str__(self):
        return f"Commessa {self.id} - {self.stage}"
