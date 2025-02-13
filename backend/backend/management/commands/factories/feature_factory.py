import random

from api.models import Category, Feature
from faker import Faker

from backend.management.commands.factories.seeder import Seeder

fake = Faker()


class FeatureFactory(Seeder):
    """Seeder for Feature table"""

    def __init__(self):
        super().__init__(Feature)

    def generate_data(self, count=20):
        categories = list(Category.objects.all())
        return [
            Feature(
                name=fake.word(),
                category=random.choice(categories) if categories else None,
            )
            for _ in range(count)
        ]
