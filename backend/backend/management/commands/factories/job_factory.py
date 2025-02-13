import random

from api.models import Customer, Job
from faker import Faker

from backend.management.commands.factories.seeder import Seeder

fake = Faker()


class JobFactory(Seeder):
    """Seeder for Job table"""

    STAGES = [
        ("estimate done", "Estimate"),
        ("estimate_accepted", "Estimate accepted"),
        ("sent_order", "Sent order"),
        ("received_cdo", "Received CDO"),
        ("confirmed_order", "Confirmed order"),
        ("arrived_goods", "Arrived goods"),
        ("closed", "Closed"),
    ]

    def __init__(self):
        super().__init__(Job)

    def generate_data(self, count=20):
        customers = list(Customer.objects.all())
        return [
            Job(
                customer=random.choice(customers),
                city=fake.city(),
                address=fake.address(),
                stage=random.choice(self.STAGES)[0],
            )
            for _ in range(count)
        ]
