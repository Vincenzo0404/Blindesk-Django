from django.core.management.base import BaseCommand

from backend.management.commands.factories import *

SEEDERS = {
    "customer": CustomerFactory,
    "category": CategoryFactory,
    "supplier": SupplierFactory,
    "product": ProductFactory,
    "order": OrderFactory,
    "orderdetail": OrderDetailFactory,
    "feature": FeatureFactory,
    "job": JobFactory,
    "monetization": MonetizationFactory,
    "productfeature": ProductFeatureFactory,
}


class Command(BaseCommand):
    help = "Popola il database con dati casuali"

    def add_arguments(self, parser):
        parser.add_argument("table", type=str, help="Nome della tabella da seedare")
        parser.add_argument(
            "--count",
            type=int,
            default=20,
            help="Numero di record da generare (default: 20)",
        )

    def handle(self, *args, **kwargs):
        table = kwargs["table"].lower()
        count = kwargs["count"]

        if table == "all":
            self.seed_all([seeder() for seeder in SEEDERS.values()])
        elif table in SEEDERS:
            seeder = SEEDERS[table]()
            seeder.seed(count)
        else:
            self.stdout.write(self.style.ERROR(f"❌ Seeder per {table} non trovato!"))

    @classmethod
    def seed_all(cls, seeders):
        """Esegue il seeding per tutte le tabelle registrate"""
        for seeder in seeders:
            seeder.seed()
        print("✅ Seeding completato per tutte le tabelle!")
