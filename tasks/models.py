from datetime import date

from django.db import models


class tarefa(models.Model):
    nome = models.CharField(
        verbose_name="Título da tarefa", max_length=100, null=False, blank=False
    )
    descricao = models.TextField(
        verbose_name="Descrição da tarefa", null=False, blank=False
    )
    data_criacao = models.DateTimeField(
        verbose_name="Data de criação", auto_now_add=True
    )
    deadline = models.DateTimeField(verbose_name="Prazo", null=True, blank=True)
    data_conclusao = models.DateTimeField(
        verbose_name="Conclusão", null=True, blank=True
    )

    def __str__(self):
        return self.nome

    class Meta:
        ordering = [
            "deadline"
        ]  # ordena as tarefas pela data de deadline, da mais próxima para a mais distante

    def mark_as_completed(self):
        if not self.data_conclusao:
            self.data_conclusao = date.today()
            self.save()
