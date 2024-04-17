# Generated by Django 5.0.4 on 2024-04-14 17:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("clinics", "0002_alter_clinichours_day_of_week"),
    ]

    operations = [
        migrations.AlterField(
            model_name="clinichours",
            name="day_of_week",
            field=models.IntegerField(
                choices=[
                    (1, "Segunda Feira"),
                    (2, "Terça Feira"),
                    (3, "Quarta Feira"),
                    (4, "Quinta Feira"),
                    (5, "Sexta Feira"),
                    (6, "Sábado"),
                    (0, "Domingo"),
                ],
                verbose_name="Dia da Semana",
            ),
        ),
    ]