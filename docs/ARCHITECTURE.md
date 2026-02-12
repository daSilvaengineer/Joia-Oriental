# 🏗️ Arquitetura do Sistema

## 1. Visão Geral

O projeto **Joia Oriental** é um e-commerce desenvolvido com Django, seguindo o padrão arquitetural MTV (Model-Template-View).

A estrutura foi organizada com foco em separação de responsabilidades e organização modular.

---

## 2. Estrutura de Camadas

O sistema está dividido nas seguintes camadas:

### Models
Responsáveis pela definição e persistência dos dados no banco.

Localização:
store/models.py

---

### Views
Responsáveis por receber requisições HTTP e retornar respostas.

As views estão organizadas por domínio:

store/views/
- product_views.py
- cart_views.py
- order_views.py
- auth_views.py
- profile_views.py

---

### Services
Camada responsável pelas regras de negócio.

Localização:
store/services/

Exemplos:
- cart_service.py
- order_service.py
- user_service.py

Essa separação evita lógica de negócio diretamente nas views.

---

### Templates
Responsáveis pela camada de apresentação (interface).

Organização:
- templates/base.html
- store/templates/store/pages/
- store/templates/store/components/

---

## 3. Fluxo Simplificado de Compra

Usuário → Produto → Carrinho → Checkout → Pedido → Banco de Dados

---

## 4. Princípios Aplicados

- Separação de responsabilidades
- Organização modular
- Estrutura preparada para escalabilidade
- Código limpo e legível
