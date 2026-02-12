# 🌸 Joia Oriental

E-commerce desenvolvido com Django como projeto acadêmico, com foco em organização de código, separação de responsabilidades e boas práticas.

---

## 🚀 Tecnologias

- Python 3
- Django
- SQLite (desenvolvimento)
- HTML, CSS e JavaScript

---

## 🏗️ Arquitetura

O projeto segue o padrão MTV do Django com organização modular:

- Models → Estrutura de dados
- Views → Camada de requisição/resposta
- Templates → Interface
- Services → Regras de negócio separadas

---

## ▶️ Como executar localmente

```bash
git clone https://github.com/seu-usuario/joia-oriental.git
cd joia-oriental

python -m venv venv
venv\Scripts\activate  # Windows

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
