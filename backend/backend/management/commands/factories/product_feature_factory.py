import random

from api.models import Feature, Product, ProductFeature
from faker import Faker

from backend.management.commands.factories.seeder import Seeder

fake = Faker()


class ProductFeatureFactory(Seeder):
    """Seeder for ProductFeature table"""

    def __init__(self):
        super().__init__(ProductFeature)

    def generate_data(self, count=30):
        products = list(Product.objects.all())
        features = list(Feature.objects.all())
        return [
            ProductFeature(
                product=random.choice(products),
                feature=random.choice(features),
                value=fake.word(),
            )
            for _ in range(count)
        ]
