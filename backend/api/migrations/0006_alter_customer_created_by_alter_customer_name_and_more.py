# Generated by Django 5.1.5 on 2025-02-08 21:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0005_rename_id_category_feature_category_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="created_by",
            field=models.ForeignKey(
                blank=True,
                default=1,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="customers",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="customer",
            name="name",
            field=models.CharField(default="New", max_length=50),
        ),
        migrations.AlterField(
            model_name="customer",
            name="province",
            field=models.CharField(default="", max_length=50),
        ),
        migrations.AlterField(
            model_name="customer",
            name="surname",
            field=models.TextField(default="Customer", max_length=50),
        ),
        migrations.AddConstraint(
            model_name="orderdetail",
            constraint=models.UniqueConstraint(
                fields=("order", "feature"), name="unique_order_feature"
            ),
        ),
    ]
