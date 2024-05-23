# Generated by Django 5.0.4 on 2024-05-23 02:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("pacientes", "0020_alter_paciente_options"),
    ]

    operations = [
        migrations.CreateModel(
            name="Transporte",
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
                ("data_de_transporte", models.DateField()),
                (
                    "motivo_de_transporte",
                    models.IntegerField(
                        choices=[
                            (1, "Retorno"),
                            (2, "Exames"),
                            (3, "Quimioterapia"),
                            (4, "Internação"),
                            (5, "Procedimento"),
                            (6, "Radioterapia"),
                            (7, "Primeira-Consulta"),
                            (8, "Outros"),
                        ]
                    ),
                ),
                ("descricao_motivo", models.CharField(max_length=60, null=True)),
                ("horario_de_atendimento", models.TimeField()),
                ("rua", models.CharField(max_length=60)),
                ("bairro", models.CharField(max_length=60)),
                ("numero", models.CharField(max_length=7)),
                ("cidade", models.CharField(max_length=60)),
                ("destino", models.CharField(max_length=60)),
                ("observação", models.CharField(max_length=60)),
                (
                    "status",
                    models.IntegerField(
                        choices=[(1, "Confirmado"), (2, "Cancelado"), (3, "Realizado")]
                    ),
                ),
                ("data_criacao", models.DateTimeField(auto_now_add=True)),
                ("data_alteracao", models.DateTimeField(auto_now=True)),
                (
                    "paciente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="pacientes.paciente",
                    ),
                ),
            ],
            options={
                "db_table": "transportes",
                "ordering": ["-data_criacao"],
            },
        ),
    ]
