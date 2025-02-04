import random

from api.models import Customer
from faker import Faker

from backend.management.commands.factories.seeder import Seeder

fake = Faker()


class CustomerFactory(Seeder):
    """Seeder for Customer table"""

    def __init__(self):
        super().__init__(Customer)

    def generate_data(self, count):
        return [
            Customer(
                name=fake.first_name(),
                surname=fake.last_name(),
                customer_type=random.choice(["B2B", "B2C"]),
                province=fake.state_abbr(),
                contact_method=random.choice(
                    ["facebook", "website", "word-of-mouth", "passerby"]
                ),
                created_by_id=1,
            )
            for _ in range(count)
        ]
