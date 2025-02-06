import random

from api.models import Job, JobStage
from faker import Faker

from backend.management.commands.factories.seeder import Seeder

fake = Faker()


class JobStageFactory(Seeder):
    """Seeder for JobStage table"""

    STAGES = [
        ("estimate done", "Estimate"),
        ("estimate_accepted", "Estimate accepted"),
        ("sent_order", "Sent order"),
        ("received_cdo", "Received CDO"),
        ("confirmed_order", "Confirmed order"),
        ("arrived_goods", "Arrived goods"),
        ("closed", "Closed"),
    ]

    def __init__(self):
        super().__init__(JobStage)

    def generate_data(self, count=5):
        return [
            JobStage(
                stage_name=fake.word(),
                position=fake.random_int(min=1, max=10),
            )
            for _ in range(count)
        ]
