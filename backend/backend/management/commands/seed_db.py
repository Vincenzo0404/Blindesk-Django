from django.core.management.base import BaseCommand

from backend.management.commands.seeders.customer_seeder import CustomerSeeder
from backend.management.commands.seeders.seeder import Seeder

SEEDERS = {
    "customer": CustomerSeeder,
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
            Seeder.seed_all([seeder() for seeder in SEEDERS.values()])
        elif table in SEEDERS:
            seeder = SEEDERS[table]()
            seeder.seed(count)
        else:
            self.stdout.write(self.style.ERROR(f"❌ Seeder per {table} non trovato!"))
