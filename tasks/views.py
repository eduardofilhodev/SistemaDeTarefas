from datetime import date

from django.shortcuts import redirect, render, get_object_or_404
from .models import tarefa
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy


def login(request):
    return render(request, "tasks/login.html")


class TarefaListView(ListView):
    model = tarefa

    def get_queryset(self):
        queryset = super().get_queryset()

        ordenar = self.request.GET.get("ordenar")

        if ordenar:
            queryset = queryset.order_by(ordenar)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_tarefas"] = tarefa.objects.count()
        return context


class TarefaCreateView(CreateView):
    model = tarefa
    fields = ["nome", "descricao", "deadline"]
    success_url = reverse_lazy("tarefa_list")


class TarefaUpdateView(UpdateView):
    model = tarefa
    fields = ["nome", "descricao", "deadline"]
    success_url = reverse_lazy("tarefa_list")


class TarefaDeleteView(DeleteView):
    model = tarefa
    success_url = reverse_lazy("tarefa_list")


class TarefaCompleteView(View):
    def get(self, request, pk):
        tarefa_obj = get_object_or_404(tarefa, pk=pk)
        tarefa_obj.mark_as_completed()
        return redirect("tarefa_list")
