from teacher.models import *

class Aula(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=255, null=False, blank=False)
    professor = models.ForeignKey(Professor, 
        on_delete=models.CASCADE, 
        related_name='aulas', 
        null=False, 
        blank=False
    )

    def __str__(self) -> str:
        return '{}'.format(self.nome)