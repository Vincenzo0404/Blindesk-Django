from django.db import models

from .category import Category


class Feature(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)
    referenced_category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="referenced_category",
        null=True,
        default=None,
    )
    name = models.CharField(max_length=255, null=True, default="Nuova caratteristica")

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["category", "name"], name="unique_feature_name"
            )
        ]

    def __str__(self):
        return self.name
