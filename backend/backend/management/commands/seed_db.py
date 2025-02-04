from django.core.management.base import BaseCommand

from backend.backend.management.commands.factories.customer_factory import (
    CustomerFactory,
)
from backend.management.commands.factories.seeder import Seeder

SEEDERS = {
    "customer": CustomerFactory,
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
