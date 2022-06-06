from django.db import models

# Create your models here.
class Tesouro(models.Model):
    nome = models.CharField(max_length=45)
    quantidade = models.IntegerField()
    preco = models.DecimalField(max_digits=10,decimal_places=2)
    
    @property
    def valor_total(self):
        valor_total = self.preco * self.quantidade
        return valor_total