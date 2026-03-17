# 📌 Sistema de Gerenciamento de Tarefas

Sistema web de gerenciamento de tarefas desenvolvido com **Django**, permitindo o controle completo de atividades, incluindo CRUD e finalização de tarefas.

A aplicação segue o padrão **MTV (Model-Template-View)** do Django e utiliza **Class-Based Views (CBVs)** para organização da lógica.

---

## ⚙️ Funcionalidades

- ✅ Cadastro de tarefas  
- 📋 Listagem de tarefas  
- ✏️ Edição de tarefas  
- ❌ Exclusão de tarefas  
- ✔️ Marcação de tarefa como concluída  
- 📅 Controle de prazo (*deadline*)  
- 🔄 Ordenação de tarefas por critérios (ex: prazo, nome, data)

---

## 🧱 Estrutura do Projeto

### Model (`tarefa`)
- Armazena:
  - nome
  - descrição
  - data de criação
  - prazo (deadline)
  - data de conclusão  
- Possui método para marcar tarefa como concluída

### Views (CBVs)
- `ListView` → listagem de tarefas  
- `CreateView` → criação de tarefas  
- `UpdateView` → edição de tarefas  
- `DeleteView` → exclusão de tarefas  
- View personalizada para conclusão de tarefas  

### Templates
- Interface desenvolvida com **Bootstrap**
- Layout base reutilizável (`base.html`)
- Páginas:
  - listagem
  - formulário (create/update)
  - confirmação de exclusão
  - login (em desenvolvimento)

---

## 🎨 Interface

- Utilização de **Bootstrap 5**
- Navbar para navegação
- Tabela para exibição das tarefas
- Botões de ação (editar, excluir, concluir)

---

## 🚧 Em desenvolvimento

- Sistema de autenticação (login)
- Melhorias de usabilidade e validações

---

## 🛠️ Tecnologias utilizadas

- Python  
- Django  
- SQLite  
- HTML  
- Bootstrap  

---

## 🎯 Objetivo

Projeto desenvolvido com foco em prática de:

- Django (CRUD completo)
- Class-Based Views (CBVs)
- Organização de código backend
- Integração entre backend e templates

---

## 📷 

<img width="1914" height="793" alt="image" src="https://github.com/user-attachments/assets/4544cb01-05b3-43d9-aa3e-29c203693b90" />
<img width="1894" height="918" alt="image" src="https://github.com/user-attachments/assets/ca58d032-33ff-4d2b-a5c2-8ebc9877c76c" />
<img width="1914" height="321" alt="image" src="https://github.com/user-attachments/assets/d4a7abbb-f7d2-493e-8016-457161ba25f5" />



