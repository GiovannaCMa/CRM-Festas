from django.db import models

class Transacao(models.Model):
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.BooleanField()  # True = entrada, False = saída
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.descricao} ({'Entrada' if self.tipo else 'Saída'})"


# Create your models here.
