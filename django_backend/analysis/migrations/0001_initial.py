# Generated by Django 5.1.3 on 2024-11-11 17:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Customer",
            fields=[
                ("customer_id", models.IntegerField(primary_key=True, serialize=False)),
                ("gender", models.CharField(max_length=10)),
                ("region", models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name="Policy",
            fields=[
                ("policy_id", models.IntegerField(primary_key=True, serialize=False)),
                ("premium", models.IntegerField()),
                ("collision", models.BooleanField(default=False)),
                ("comprehensive", models.BooleanField(default=False)),
                (
                    "customer_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="policies",
                        to="analysis.customer",
                    ),
                ),
            ],
        ),
    ]
