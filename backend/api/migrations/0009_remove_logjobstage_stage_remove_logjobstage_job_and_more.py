# Generated by Django 5.1.5 on 2025-02-13 21:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0008_alter_category_name_alter_category_type_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="logjobstage",
            name="stage",
        ),
        migrations.RemoveField(
            model_name="logjobstage",
            name="job",
        ),
        migrations.AddField(
            model_name="job",
            name="stage",
            field=models.CharField(
                choices=[
                    ("new", "Nuova"),
                    ("in_progress", "In corso"),
                    ("completed", "Completata"),
                    ("cancelled", "Annullata"),
                ],
                default="new",
                max_length=255,
            ),
        ),
        migrations.DeleteModel(
            name="JobStage",
        ),
        migrations.DeleteModel(
            name="LogJobStage",
        ),
    ]
