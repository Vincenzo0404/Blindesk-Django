import random

from api.models import Category, Product, Supplier
from faker import Faker

from backend.management.commands.factories.seeder import Seeder

fake = Faker()


class ProductFactory(Seeder):
    """Seeder for Product table"""

    def __init__(self):
        super().__init__(Product)

    def generate_data(self, count=15):
        categories = list(Category.objects.all())
        suppliers = list(Supplier.objects.all())
        return [
            Product(
                name=fake.word(),
                id_category=random.choice(categories),
                id_supplier=random.choice(suppliers),
            )
            for _ in range(count)
        ]
