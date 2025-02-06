import random

from api.models import Job, Order, Product
from faker import Faker

from backend.management.commands.factories.seeder import Seeder

fake = Faker()


class OrderFactory(Seeder):
    """Seeder for Order table"""

    def __init__(self):
        super().__init__(Order)

    def generate_data(self, count=100):
        jobs = list(Job.objects.all())
        products = list(Product.objects.all())
        return [
            Order(
                id_job=random.choice(jobs),
                id_product=random.choice(products),
                q_t=fake.random_int(min=1, max=20),
                discount=fake.random_int(min=0, max=100),
            )
            for _ in range(count)
        ]
