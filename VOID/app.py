"""
VOID — Loja de roupas alternativa (Y2K • Grunge • Vintage • Dark Goth)
Projeto acadêmico — FATEC
Backend: Python + Flask | Templates: Jinja2 | Estilo: Bootstrap 5
Os dados ficam em listas Python (memória) enquanto a aplicação estiver rodando.
"""
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "void-chave-academica"

# ------------------------------------------------------------------
# DADOS FICTÍCIOS (em memória)
# ------------------------------------------------------------------
usuarios = [
    {"id": 1, "nome": "Usuário 1", "email": "user1@example.com", "celular": "11999999999",
     "nascimento": "2000-05-10", "cpf": "111.111.111-11", "nivel": "Usuário", "cep": "01001-000",
     "endereco": "Rua Augusta", "numero": "100", "complemento": "Apto 1", "cidade": "São Paulo", "estado": "SP"},
    {"id": 2, "nome": "Usuário 2", "email": "user2@example.com", "celular": "11988888888",
     "nascimento": "1998-11-22", "cpf": "222.222.222-22", "nivel": "Administrador", "cep": "20040-000",
     "endereco": "Av. Rio Branco", "numero": "250", "complemento": "", "cidade": "Rio de Janeiro", "estado": "RJ"},
    {"id": 3, "nome": "Raven Black", "email": "raven@example.com", "celular": "11977777777",
     "nascimento": "2002-10-31", "cpf": "333.333.333-33", "nivel": "Usuário", "cep": "30110-000",
     "endereco": "Rua da Bahia", "numero": "13", "complemento": "Casa", "cidade": "Belo Horizonte", "estado": "MG"},
]

produtos = [
    {"id": 1, "nome": "Baby Tee Dark Angel", "categoria": "Dark Goth", "tamanho": "P", "cor": "Preto",
     "preco": 89.90, "estoque": 15, "descricao": "Baby tee com estampa de anjo gótico.", "imagem": ""},
    {"id": 2, "nome": "Calça Cargo Y2K", "categoria": "Y2K", "tamanho": "M", "cor": "Preto",
     "preco": 179.90, "estoque": 8, "descricao": "Calça cargo cintura baixa estilo anos 2000.", "imagem": ""},
    {"id": 3, "nome": "Saia Xadrez Grunge", "categoria": "Grunge", "tamanho": "P", "cor": "Vermelho/Preto",
     "preco": 119.90, "estoque": 12, "descricao": "Saia xadrez com correntes.", "imagem": ""},
    {"id": 4, "nome": "Camiseta Oversized Skull", "categoria": "Dark Goth", "tamanho": "G", "cor": "Preto",
     "preco": 99.90, "estoque": 20, "descricao": "Camiseta oversized com caveira.", "imagem": ""},
    {"id": 5, "nome": "Jaqueta Vintage Leather", "categoria": "Vintage", "tamanho": "M", "cor": "Marrom",
     "preco": 349.90, "estoque": 4, "descricao": "Jaqueta de couro estilo vintage.", "imagem": ""},
]

pedidos = [
    {"id": 1, "numero": "#001", "cliente": "Usuário 1", "produto": "Baby Tee Dark Angel",
     "quantidade": 1, "valor": 89.90, "status": "Pago", "data": "2026-10-05"},
    {"id": 2, "numero": "#002", "cliente": "Usuário 2", "produto": "Jaqueta Vintage Leather",
     "quantidade": 1, "valor": 349.90, "status": "Enviado", "data": "2026-10-03"},
    {"id": 3, "numero": "#003", "cliente": "Raven Black", "produto": "Saia Xadrez Grunge",
     "quantidade": 2, "valor": 239.80, "status": "Pendente", "data": "2026-10-06"},
    {"id": 4, "numero": "#004", "cliente": "Usuário 1", "produto": "Calça Cargo Y2K",
     "quantidade": 1, "valor": 179.90, "status": "Entregue", "data": "2026-09-28"},
]

ESTADOS = ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA",
           "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"]
CATEGORIAS = ["Y2K", "Grunge", "Vintage", "Dark Goth"]
TAMANHOS = ["PP", "P", "M", "G", "GG"]
STATUS = ["Pendente", "Pago", "Enviado", "Entregue", "Cancelado"]


# ------------------------------------------------------------------
# FUNÇÕES AUXILIARES
# ------------------------------------------------------------------
def buscar(lista, id):
    """Retorna o item da lista com o id informado (ou None)."""
    for item in lista:
        if item["id"] == id:
            return item
    return None


def proximo_id(lista):
    return max([item["id"] for item in lista], default=0) + 1


def para_float(valor):
    try:
        return float(str(valor).replace(",", "."))
    except ValueError:
        return 0.0


def para_int(valor):
    try:
        return int(valor)
    except ValueError:
        return 0


@app.template_filter("moeda")
def moeda(valor):
    """Formata número como R$ 0,00."""
    return "R$ {:,.2f}".format(valor).replace(",", "X").replace(".", ",").replace("X", ".")


@app.template_filter("data_br")
def data_br(valor):
    """Converte AAAA-MM-DD para DD/MM/AAAA."""
    try:
        a, m, d = valor.split("-")
        return f"{d}/{m}/{a}"
    except (ValueError, AttributeError):
        return valor


# ------------------------------------------------------------------
# LOGIN (template SEM menu)
# ------------------------------------------------------------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Autenticação simplificada (projeto acadêmico)
        return redirect(url_for("index"))
    return render_template("login.html")


@app.route("/sair")
def sair():
    return redirect(url_for("login"))


# ------------------------------------------------------------------
# PÁGINA INICIAL / DASHBOARD
# ------------------------------------------------------------------
@app.route("/")
def index():
    return render_template("index.html", total_usuarios=len(usuarios),
                           total_produtos=len(produtos), total_pedidos=len(pedidos),
                           destaques=produtos[:4])


# ------------------------------------------------------------------
# USUÁRIOS (CRUD)
# ------------------------------------------------------------------
def dados_usuario():
    campos = ["nome", "email", "celular", "nascimento", "cpf", "nivel", "cep",
              "endereco", "numero", "complemento", "cidade", "estado"]
    return {c: request.form.get(c, "").strip() for c in campos}


@app.route("/usuarios")
def listar_usuarios():
    return render_template("usuarios/listar.html", usuarios=usuarios)


@app.route("/usuarios/cadastrar", methods=["GET", "POST"])
def cadastrar_usuario():
    if request.method == "POST":
        novo = dados_usuario()
        novo["id"] = proximo_id(usuarios)
        usuarios.append(novo)
        flash("Usuário cadastrado com sucesso!", "success")
        return redirect(url_for("listar_usuarios"))
    return render_template("usuarios/cadastrar.html", usuario=None, estados=ESTADOS)


@app.route("/usuarios/editar/<int:id>", methods=["GET", "POST"])
def editar_usuario(id):
    usuario = buscar(usuarios, id)
    if usuario is None:
        flash("Usuário não encontrado.", "danger")
        return redirect(url_for("listar_usuarios"))
    if request.method == "POST":
        usuario.update(dados_usuario())
        flash("Usuário atualizado com sucesso!", "success")
        return redirect(url_for("listar_usuarios"))
    return render_template("usuarios/cadastrar.html", usuario=usuario, estados=ESTADOS)


@app.route("/usuarios/excluir/<int:id>")
def excluir_usuario(id):
    usuario = buscar(usuarios, id)
    if usuario:
        usuarios.remove(usuario)
        flash("Usuário excluído.", "warning")
    return redirect(url_for("listar_usuarios"))


# ------------------------------------------------------------------
# PRODUTOS (CRUD)
# ------------------------------------------------------------------
def dados_produto():
    return {
        "nome": request.form.get("nome", "").strip(),
        "categoria": request.form.get("categoria", ""),
        "tamanho": request.form.get("tamanho", ""),
        "cor": request.form.get("cor", "").strip(),
        "preco": para_float(request.form.get("preco", "0")),
        "estoque": para_int(request.form.get("estoque", "0")),
        "descricao": request.form.get("descricao", "").strip(),
        "imagem": request.form.get("imagem", "").strip(),
    }


@app.route("/produtos")
def listar_produtos():
    return render_template("produtos/listar.html", produtos=produtos)


@app.route("/produtos/cadastrar", methods=["GET", "POST"])
def cadastrar_produto():
    if request.method == "POST":
        novo = dados_produto()
        novo["id"] = proximo_id(produtos)
        produtos.append(novo)
        flash("Produto cadastrado com sucesso!", "success")
        return redirect(url_for("listar_produtos"))
    return render_template("produtos/cadastrar.html", produto=None,
                           categorias=CATEGORIAS, tamanhos=TAMANHOS)


@app.route("/produtos/editar/<int:id>", methods=["GET", "POST"])
def editar_produto(id):
    produto = buscar(produtos, id)
    if produto is None:
        flash("Produto não encontrado.", "danger")
        return redirect(url_for("listar_produtos"))
    if request.method == "POST":
        produto.update(dados_produto())
        flash("Produto atualizado com sucesso!", "success")
        return redirect(url_for("listar_produtos"))
    return render_template("produtos/cadastrar.html", produto=produto,
                           categorias=CATEGORIAS, tamanhos=TAMANHOS)


@app.route("/produtos/excluir/<int:id>")
def excluir_produto(id):
    produto = buscar(produtos, id)
    if produto:
        produtos.remove(produto)
        flash("Produto excluído.", "warning")
    return redirect(url_for("listar_produtos"))


# ------------------------------------------------------------------
# PEDIDOS (CRUD)
# ------------------------------------------------------------------
def dados_pedido():
    return {
        "numero": request.form.get("numero", "").strip(),
        "cliente": request.form.get("cliente", ""),
        "produto": request.form.get("produto", ""),
        "quantidade": para_int(request.form.get("quantidade", "1")),
        "valor": para_float(request.form.get("valor", "0")),
        "status": request.form.get("status", "Pendente"),
        "data": request.form.get("data", ""),
    }


@app.route("/pedidos")
def listar_pedidos():
    return render_template("pedidos/listar.html", pedidos=pedidos)


@app.route("/pedidos/cadastrar", methods=["GET", "POST"])
def cadastrar_pedido():
    if request.method == "POST":
        novo = dados_pedido()
        novo["id"] = proximo_id(pedidos)
        pedidos.append(novo)
        flash("Pedido cadastrado com sucesso!", "success")
        return redirect(url_for("listar_pedidos"))
    return render_template("pedidos/cadastrar.html", pedido=None, usuarios=usuarios,
                           produtos=produtos, status_lista=STATUS)


@app.route("/pedidos/editar/<int:id>", methods=["GET", "POST"])
def editar_pedido(id):
    pedido = buscar(pedidos, id)
    if pedido is None:
        flash("Pedido não encontrado.", "danger")
        return redirect(url_for("listar_pedidos"))
    if request.method == "POST":
        pedido.update(dados_pedido())
        flash("Pedido atualizado com sucesso!", "success")
        return redirect(url_for("listar_pedidos"))
    return render_template("pedidos/cadastrar.html", pedido=pedido, usuarios=usuarios,
                           produtos=produtos, status_lista=STATUS)


@app.route("/pedidos/excluir/<int:id>")
def excluir_pedido(id):
    pedido = buscar(pedidos, id)
    if pedido:
        pedidos.remove(pedido)
        flash("Pedido excluído.", "warning")
    return redirect(url_for("listar_pedidos"))


if __name__ == "__main__":
    app.run(debug=True)
