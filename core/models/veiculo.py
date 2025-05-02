from django.db import models

class Veiculo(models.Model):
   ano = models.IntegerField(null=True, blank=True, default=0)
   preco = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0)
   modelo = models.ForeignKey('Modelo', on_delete=models.CASCADE)
   cor = models.ForeignKey('Cor', on_delete=models.CASCADE)
   acessorios = models.ManyToManyField('Acessorio', blank=True)

   def __str__(self):
    return f"Id: {self.id} | Modelo: {self.modelo} | Cor: {self.cor} | Ano: {self.ano}"
    