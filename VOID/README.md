# VOID — Loja de Roupas Alternativa

**Y2K • GRUNGE • VINTAGE • DARK GOTH**

Projeto acadêmico — FATEC

## Objetivo
Desenvolver um sistema web simples em **Python + Flask** para uma loja de roupas alternativa, com
login, menu de navegação e CRUD (Cadastrar, Listar, Editar e Excluir) de **Usuários**, **Produtos** e **Pedidos**.

## Tema
A VOID é uma loja de moda underground com peças inspiradas nos estilos Y2K, Grunge, Vintage e Dark Goth.
Paleta: preto, cinza escuro, vinho, vermelho escuro, branco e detalhes prateados.

## Tecnologias utilizadas
- Python 3
- Flask (rotas, `render_template`, `request.form`, `redirect`, `url_for`, `flash`)
- Jinja2 (`extends`, `block`, `for`, `if`, variáveis, filtros)
- HTML5 e CSS3
- Bootstrap 5 (via CDN): Navbar, Dropdown, Container, Card, Table, Form, Button, Badge, Alert
- JavaScript (apenas para confirmar exclusões e calcular o valor total do pedido)

Os dados ficam em **listas Python em memória** (já preenchidas com dados fictícios).
Ao reiniciar a aplicação, os dados voltam ao estado inicial.

## Estrutura do projeto
```
VOID/
├── app.py                 # Aplicação Flask e todas as rotas
├── requirements.txt
├── README.md
├── .gitignore
├── templates/
│   ├── base.html          # Template COM menu superior
│   ├── login.html         # Template SEM menu superior
│   ├── index.html         # Página inicial / dashboard
│   ├── usuarios/  (listar.html, cadastrar.html)
│   ├── produtos/  (listar.html, cadastrar.html)
│   └── pedidos/   (listar.html, cadastrar.html)
└── static/
    ├── css/style.css
    ├── js/script.js
    └── img/banner.jpg
```

## Rotas
| Rota | Descrição |
|------|-----------|
| `/login` | Login (sem menu) |
| `/` | Página inicial |
| `/sair` | Volta ao login |
| `/usuarios` | Listagem de usuários |
| `/usuarios/cadastrar` | Cadastro de usuário |
| `/usuarios/editar/<id>` | Edição de usuário |
| `/usuarios/excluir/<id>` | Exclusão de usuário |
| `/produtos`, `/produtos/cadastrar`, `/produtos/editar/<id>`, `/produtos/excluir/<id>` | CRUD de produtos |
| `/pedidos`, `/pedidos/cadastrar`, `/pedidos/editar/<id>`, `/pedidos/excluir/<id>` | CRUD de pedidos |

## Como executar

### 1. Criar o ambiente virtual
```bash
python -m venv venv
```

### 2. Ativar o ambiente virtual
No Windows:
```bash
venv\Scripts\activate
```
No Linux/Mac:
```bash
source venv/bin/activate
```

### 3. Instalar as dependências
```bash
pip install -r requirements.txt
```

### 4. Executar
```bash
python app.py
```

### 5. Acessar no navegador
- http://127.0.0.1:5000/login (tela de login)
- http://127.0.0.1:5000/ (página inicial)

Qualquer e-mail e senha permitem entrar (autenticação simplificada para fins acadêmicos).

## Como utilizar o Git e enviar para o GitHub
1. Crie um repositório vazio no GitHub.
2. Na pasta do projeto, execute:

```bash
git init
git add .
git commit -m "Projeto inicial"
git branch -M main
git remote add origin URL_DO_REPOSITORIO
git push -u origin main
```

Para enviar novas alterações depois:
```bash
git add .
git commit -m "Descrição da alteração"
git push
```

## Requisitos atendidos
- [x] Flask + Python
- [x] Ambiente virtual
- [x] Git / GitHub
- [x] Template com menu superior (`base.html`) e sem menu (`login.html`)
- [x] Listagem e cadastro de Usuários, Produtos e Pedidos
- [x] Rotas Flask e navegação pelo menu com `url_for()`
- [x] Bootstrap 5 e Jinja2
- [x] Formulários com método POST
- [x] CRUD básico
