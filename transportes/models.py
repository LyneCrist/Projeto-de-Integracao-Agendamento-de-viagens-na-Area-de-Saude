from django.db import models
from pacientes.models import Paciente


class Transporte(models.Model):

    MOTIVO_CHOICES = (
        (1, "Retorno"),
        (2, "Exames"),
        (3, "Quimioterapia"),
        (4, "Internação"),
        (5, "Procedimento"),
        (6, "Radioterapia"),
        (7, "Primeira-Consulta"),
        (8, "Outros"),
    )

    STATUS_CHOICES = ((1, "Confirmado"), (2, "Cancelado"), (3, "Realizado"))

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)

    data_de_transporte = models.DateField()

    horario_de_atendimento = models.TimeField()

    motivo_de_transporte = models.IntegerField(choices=MOTIVO_CHOICES)

    descricao_motivo = models.CharField(max_length=60, null=True)

    rua = models.CharField(max_length=60)

    bairro = models.CharField(max_length=60)

    numero = models.CharField(max_length=7)

    cidade = models.CharField(max_length=60)

    destino = models.CharField(max_length=60)

    observacao = models.CharField(max_length=60)

    status = models.IntegerField(choices=STATUS_CHOICES)

    data_criacao = models.DateTimeField(auto_now_add=True)

    data_alteracao = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "transportes"
        ordering = ["-data_criacao"]
