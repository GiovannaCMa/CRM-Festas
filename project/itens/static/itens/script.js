
      // conexao com o html
      console.log("JS carregado!");

      document.addEventListener("DOMContentLoaded", function () {
        const btnApply = document.querySelector(".btn-primary");
        const btnLimpar = document.querySelector(".btn-secondary");
        const itensContainer = document.querySelector(".itens-container");

        // Dropdown de ordenação
        const dropdown = document.querySelector(".dropdown-field1");
        const orderButton = dropdown
          ? dropdown.querySelector(".order-button")
          : null;
        const orderMenu = dropdown
          ? dropdown.querySelector(".order-menu")
          : null;
        const radios = dropdown
          ? dropdown.querySelectorAll(".order-menu input[type='radio']")
          : [];

        if (dropdown && orderButton && orderMenu) {
          // Abrir/fechar somente ao clicar no botão
          orderButton.addEventListener("click", function (e) {
            e.stopPropagation();
            const willOpen = !dropdown.classList.contains("open");
            dropdown.classList.toggle("open", willOpen);
            orderButton.setAttribute("aria-expanded", String(willOpen));
          });

          // Tornar toda a área da dropdown clicável (exceto o menu)
          dropdown.addEventListener("click", function (e) {
            if (orderMenu.contains(e.target)) return; // não propaga para o botão ao clicar dentro do menu
            if (e.target === orderButton) return; // já tratado acima
            e.stopPropagation();
            orderButton.click();
          });

          // Evitar que cliques dentro do menu fechem ao borbulhar
          orderMenu.addEventListener("click", function (e) {
            e.stopPropagation();
          });

          // Seleção de opção: atualiza texto do botão e fecha
          radios.forEach(function (radio) {
            radio.addEventListener("change", function () {
              const selectedLabel = radio.closest("label");
              if (selectedLabel && orderButton) {
                orderButton.textContent = selectedLabel.textContent.trim();
              }
              dropdown.classList.remove("open");
              orderButton.setAttribute("aria-expanded", "false");
            });
          });

          // Fechar ao clicar fora
          document.addEventListener("click", function () {
            dropdown.classList.remove("open");
            if (orderButton) orderButton.setAttribute("aria-expanded", "false");
          });
        }

        // Função para adicionar item
        if (btnApply && itensContainer) {
          btnApply.addEventListener("click", function () {
            // Pegar o item original (modelo)
            const itemOriginal = document.getElementById("item-original");

            if (itemOriginal) {
              // Verificar se já existe pelo menos um item adicionado
              const itensExistentes = itensContainer.querySelectorAll(
                ".item-row:not(#item-original)"
              );

              // Se já existir pelo menos um item, adicionar linha divisória
              if (itensExistentes.length > 0) {
                const linhaDivisoria = document.createElement("div");
                linhaDivisoria.className = "linha-horizontal-cinza";
                itensContainer.appendChild(linhaDivisoria);
              }

              const novoItem = itemOriginal.cloneNode(true);
              // Remover o ID do novo item para não ter duplicatas
              novoItem.removeAttribute("id");
              // Forçar o display para block explicitamente
              novoItem.style.display = "";
              // Remover a borda inferior do item-row
              novoItem.style.borderBottom = "none";

              // Adicionar o novo item
              itensContainer.appendChild(novoItem);

              // Re-inicializar os ícones do Lucide para o novo item
              lucide.createIcons();
            }
          });
        }

        // Função para limpar todos os itens
        if (btnLimpar && itensContainer) {
          btnLimpar.addEventListener("click", function () {
            // Encontrar todos os itens e linhas divisórias (exceto o item original)
            const todasAsLinhas = itensContainer.querySelectorAll(
              ".linha-horizontal-cinza"
            );
            const todosOsItens = itensContainer.querySelectorAll(
              ".item-row:not(#item-original)"
            );

            // Remover todas as linhas divisórias
            todasAsLinhas.forEach(function (linha) {
              linha.remove();
            });

            // Remover todos os itens adicionados
            todosOsItens.forEach(function (item) {
              item.remove();
            });
          });
        }
      });


function abrirModal(id, nome) {
    document.getElementById("modalTexto").innerText =
        "Tem certeza que deseja excluir o item: " + nome + "?";

    document.getElementById("formExcluir").dataset.url =
        `/itens/excluir/${id}/`;

    document.getElementById("modalExcluir").style.display = "flex";
}


function fecharModal() {
    document.getElementById("modalExcluir").style.display = "none";
}
function confirmarExclusao() {
    const url = document.getElementById("formExcluir").dataset.url;

    if (!url) {
        console.error("ERRO: URL de exclusão não encontrada!");
        return;
    }

    const form = document.createElement("form");
    form.method = "POST";
    form.action = url;

    const csrf = document.querySelector("[name=csrfmiddlewaretoken]").cloneNode();
    form.appendChild(csrf);

    document.body.appendChild(form);
    form.submit();
}
