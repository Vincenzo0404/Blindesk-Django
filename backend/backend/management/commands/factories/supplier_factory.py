from api.models import Supplier
from faker import Faker

from backend.management.commands.factories.seeder import Seeder

fake = Faker()


class SupplierFactory(Seeder):
    """Seeder for Supplier table"""

    def __init__(self):
        super().__init__(Supplier)

    def generate_data(self, count=5):
        return [
            Supplier(
                name=fake.company(),
            )
            for _ in range(count)
        ]
