import random

from api.models import Monetization, Product
from faker import Faker

from backend.management.commands.factories.seeder import Seeder

fake = Faker()


class MonetizationFactory(Seeder):
    """Seeder for Monetization table"""

    def __init__(self):
        super().__init__(Monetization)

    def generate_data(self, count=60):
        products = list(Product.objects.all())
        unit_cost = fake.pydecimal(left_digits=5, right_digits=2, positive=True)
        unit_price = unit_cost + fake.pydecimal(
            left_digits=5, right_digits=2, positive=True
        )
        return [
            Monetization(
                id_product=random.choice(products),
                unit_cost=unit_cost,
                unit_price=unit_price,
                started_at=fake.date_time(),
                ended_at=fake.date_time(),
            )
            for _ in range(count)
        ]
