import random

from api.models import Customer, Job
from faker import Faker

from backend.management.commands.factories.seeder import Seeder

fake = Faker()


class JobFactory(Seeder):
    """Seeder for Job table"""

    def __init__(self):
        super().__init__(Job)

    def generate_data(self, count=20):
        customers = list(Customer.objects.all())
        return [
            Job(
                id_customer=random.choice(customers),
                city=fake.city(),
                address=fake.address(),
            )
            for _ in range(count)
        ]
