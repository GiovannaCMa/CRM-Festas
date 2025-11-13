from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    # outros campos do cliente...

    def __str__(self):
        return self.nome

class Festa(models.Model):
    nome_festa = models.CharField(max_length=100)
    data = models.DateField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome_festa} - {self.data}"
