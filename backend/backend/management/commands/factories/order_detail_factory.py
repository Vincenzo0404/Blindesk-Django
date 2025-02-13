import random

from api.models import Feature, Order, OrderDetail
from faker import Faker

from backend.management.commands.factories.seeder import Seeder

fake = Faker()


class OrderDetailFactory(Seeder):
    """Seeder for OrderDetail table"""

    def __init__(self):
        super().__init__(OrderDetail)

    # TODO: CORRECT THIS
    def generate_data(self, count=30):
        orders = list(Order.objects.all())
        features = list(Feature.objects.all())
        # order = random.choice(orders)
        # feature = random.choice(order.id_product.id_category.features)
        return [
            OrderDetail(
                order=random.choice(orders),
                feature=random.choice(features),
                value=fake.word(),
            )
            for _ in range(count)
        ]
