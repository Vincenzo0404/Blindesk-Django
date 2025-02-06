from abc import ABC, abstractmethod


class Seeder(ABC):
    """Classe base per tutti i Seeder"""

    default_count = 20

    def __init__(self, model):
        self.model = model
        self.name = model.__name__

    @abstractmethod
    def generate_data(self):
        """Metodo che deve essere implementato nei seeder specifici"""
        pass

    def seed(self, count=20):
        """Esegue il seeding della tabella"""
        print(f"🔄 Seeding {self.name}...")

        self.model.objects.bulk_create(self.generate_data())

        print(f"✅ {self.name} seed completato! ({count} record)")
