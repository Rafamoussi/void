// VOID — JavaScript usado apenas onde é necessário

// 1) Confirmação antes de excluir um registro
document.querySelectorAll(".btn-excluir").forEach(function (botao) {
  botao.addEventListener("click", function (evento) {
    if (!confirm("Tem certeza que deseja excluir este registro?")) {
      evento.preventDefault();
    }
  });
});

// 2) Cálculo automático do valor total no cadastro de pedidos
const produto = document.getElementById("produto");
const quantidade = document.getElementById("quantidade");
const valor = document.getElementById("valor");

function calcularTotal() {
  const opcao = produto.options[produto.selectedIndex];
  if (!opcao) return;
  const preco = parseFloat(opcao.dataset.preco || 0);
  const qtd = parseInt(quantidade.value || 0);
  valor.value = (preco * qtd).toFixed(2);
}

if (produto && quantidade && valor && opcaoTemPreco()) {
  produto.addEventListener("change", calcularTotal);
  quantidade.addEventListener("input", calcularTotal);
  if (!valor.value) calcularTotal();
}

function opcaoTemPreco() {
  return produto.options.length && produto.options[0].dataset.preco !== undefined;
}
