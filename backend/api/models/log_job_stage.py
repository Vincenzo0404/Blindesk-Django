from django.db import models

from .job import Job
from .job_stage import JobStage


class LogJobStage(models.Model):
    id = models.AutoField(primary_key=True)
    id_job = models.ForeignKey(Job, on_delete=models.CASCADE)
    id_stage = models.ForeignKey(JobStage, on_delete=models.CASCADE)
    status = models.CharField(max_length=255)
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.stage
