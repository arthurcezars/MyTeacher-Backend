from teacher.models import *

class Professor(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    valor_hora = models.DecimalField(max_digits=9, decimal_places=2, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    foto = models.URLField(max_length=255, null=False, blank=False)

    def __str__(self):
        return '{}'.format(self.nome)