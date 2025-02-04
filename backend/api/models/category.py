from django.db import models


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    type = models.CharField(
        max_length=50, choices=[("good", "Good"), ("service", "Service")]
    )

    def __str__(self):
        return self.nome
