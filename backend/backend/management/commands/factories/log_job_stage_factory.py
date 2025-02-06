import random

from api.models import Job, JobStage, LogJobStage
from faker import Faker

from backend.management.commands.factories.seeder import Seeder

fake = Faker()


class LogJobStageFactory(Seeder):
    """Seeder for LogJobStage table"""

    def __init__(self):
        super().__init__(LogJobStage)

    def generate_data(self, count=100):
        job = list(Job.objects.all())
        stage = list(JobStage.objects.all())
        return [
            LogJobStage(
                id_job=random.choice(job),
                id_stage=random.choice(stage),
                started_at=fake.date_time(),
                ended_at=fake.date_time(),
            )
            for _ in range(count)
        ]
