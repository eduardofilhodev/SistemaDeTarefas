"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from tasks.views import (
    TarefaCreateView,
    TarefaDeleteView,
    TarefaListView,
    TarefaUpdateView,
    TarefaCompleteView,
    login,
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", login, name="login"),
    path(
        "lista", TarefaListView.as_view(), name="tarefa_list"
    ),  # da pra colocar o template_name = "tasks/tarefa_list.html" pra especificar o template, mas como o nome é igual ao modelo, ele já acha
    path("criar/", TarefaCreateView.as_view(), name="tarefa_create"),
    path("editar/<int:pk>/", TarefaUpdateView.as_view(), name="tarefa_update"),
    path("excluir/<int:pk>/", TarefaDeleteView.as_view(), name="tarefa_delete"),
    path("concluir/<int:pk>/", TarefaCompleteView.as_view(), name="tarefa_complete"),
]
