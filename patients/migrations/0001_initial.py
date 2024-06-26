# Generated by Django 5.0.4 on 2024-06-23 22:16

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Patient",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="Name")),
                (
                    "country_code",
                    models.CharField(
                        choices=[("+55", "Brasil (+55)")],
                        default="+55",
                        max_length=5,
                        verbose_name="Código do País",
                    ),
                ),
                ("phone", models.CharField(max_length=20, verbose_name="Telefone")),
                ("email", models.EmailField(max_length=254, verbose_name="Email")),
                ("birth_date", models.DateField(verbose_name="Data de nascimento")),
            ],
            options={
                "verbose_name": "Paciente",
                "verbose_name_plural": "Pacientes",
            },
        ),
        migrations.CreateModel(
            name="PatientProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("can_send_mail", models.BooleanField()),
                ("can_send_whatsapp_message", models.BooleanField()),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="patient_profile",
                        to="patients.patient",
                        verbose_name="Configurações do Paciente",
                    ),
                ),
            ],
        ),
    ]
