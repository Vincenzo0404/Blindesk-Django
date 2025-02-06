import random

from api.models import Category
from faker import Faker

from backend.management.commands.factories.seeder import Seeder

fake = Faker()


class CategoryFactory(Seeder):
    """Seeder for Category table"""

    def __init__(self):
        super().__init__(Category)

    def generate_data(self, count=3):
        return [
            Category(
                name=fake.word(),
                type=random.choice(["good", "service"]),
            )
            for _ in range(count)
        ]
