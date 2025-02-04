from django.db import models

from .feature import Feature
from .order import Order
from .product_feature import ProductFeature


class OrderDetail(models.Model):
    id = models.AutoField(primary_key=True)
    id_order = models.ForeignKey(Order, on_delete=models.CASCADE)
    id_feature = models.ForeignKey(Feature, on_delete=models.CASCADE)
    value = models.CharField(max_length=255)

    def __str__(self):
        return f"Order {self.id_order.id} - {self.id_feature.name}: {self.value}"

    # TODO: Implement this method
    # def get_optional_features(self, include_mandatory=False) -> listFeature]:
    #     """
    #     Returns:
    #         A list of missing feature values which may be defined in the order.
    #     """

    # returnFeature.objects.filter(
    #     id=self.id_order.id,
    #     id_category_feature=self.id_feature,
    # )
