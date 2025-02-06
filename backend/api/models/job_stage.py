from django.db import models

from .job import Job


class JobStage(models.Model):
    id = models.AutoField(primary_key=True)
    stage_name = models.CharField(max_length=255)
    position = models.IntegerField(default=id)

    def __str__(self):
        return f"{self.job} - {self.stage_name}"
