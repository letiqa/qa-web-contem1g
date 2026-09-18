# 🧪 Test Report — Contem1g.com.br

> **Projeto:** Testes de automação  com Playwright
> **Site testado:** [contem1g.com.br](https://www.contem1g.com.br)  
> **Tipo de teste:** Performance + automação + teste exploratório
> **Status geral:** ✅

---

## 📋 Sumário Executivo

Este relatório documenta os defeitos encontrados durante a execução de um smoke test e testes automatizados no site **contem1g.com.br**. Foram feitos 21 testes cobrindo o principal nas áreas de busca, carrinho de compras, cadastro de usuário e performance. Testes de checkout e testes sobre pedidos foram excluídos do escopo por envolverem compra ou pedidos anteriores. Todos os casos de teste estão disponiveis na [Planilha de Testes](https://docs.google.com/spreadsheets/d/1bGlZ2A-0kKkkLccOxovWpXP5Dfr_3PLK-k-ibW-eLj8/edit?usp=sharing). 


# 🐞 Relatório de Bugs e Melhorias

> 📌 **Nota:** Os comportamentos documentados neste relatório refletem o estado do sistema durante o ciclo de testes executado.

---

## 🐛 Bug 01: Inconsistência de UI no botão "Olhadinha" no carrossel

**Status:** 🟢 Fechado / Corrigido

**Severidade:** Baixa (Minor)

**Ambiente:** Web / [Navegador e Versão] / [Resolução da Tela]

### Pré-condições:
* Estar na página Home do site [https://www.contem1g.com.br](https://www.contem1g.com.br).

### Passos para reproduzir:
1. Acesse a página Home do site.
2. Role a página até encontrar a seção/carrossel "LANÇAMENTO: MÁSCARA EYECONIC".
3. Observe os cards dos produtos exibidos no carrossel.
4. Verifique a presença do botão "Olhadinha" em cada item.

### Resultado Esperado:
Todos os produtos pertencentes ao carrossel devem apresentar o mesmo padrão de interface, exibindo o botão "Olhadinha".

### Resultado Atual:
Há uma inconsistência na interface. Somente o produto específico "Mascara para cilios EYEconic" apresenta o botão "Olhadinha". Os demais produtos do mesmo carrossel não possuem o botão.

---

## 🐛 Bug 02: Falha na validação e aplicação do Cupom de Desconto

**Status:** 🔴 Aberto

**Severidade:** Alta

**Ambiente:** Web / [Navegador e Versão]

### Pré-condições:
* Ter pelo menos um item adicionado ao carrinho de compras.

### Passos para reproduzir:
1. Acesse o carrinho de compras.
2. Localize o campo destinado à inserção de cupons de desconto.
3. Insira um texto aleatório/inválido (ex: "TESTE123") e clique em aplicar.
4. Observe que o sistema salva a inserção e exibe a mensagem: "* será validado na próxima etapa".
5. Clique para avançar para a etapa de finalização da compra (checkout).
6. Verifique o resumo do pedido e os valores aplicados.

### Resultado Esperado:
O sistema deve validar o texto inserido no momento do clique, exibindo uma mensagem de erro caso o cupom seja inválido. Caso o cupom seja válido, o desconto correspondente deve ser exibido na tela de finalização da compra.

### Resultado Atual:
O campo de cupom carece de validação no front-end/back-end, aceitando qualquer texto inserido. O sistema exibe a mensagem de que será validado na próxima etapa, porém, ao chegar na finalização da compra, o cupom não é exibido e nenhum cálculo de desconto ou feedback de erro é apresentado ao usuário.

---

## 🛠️ Melhoria Técnica: Performance e Acessibilidade (Lighthouse)

**Status:** 🔴 Aberto

**Tipo:** Débito Técnico / Melhoria

### Evidências do Lighthouse:
* **Desempenho Geral:** Nota 37 (Ruim).
* **LCP (Largest Contentful Paint):** O conteúdo principal demora aproximadamente 4,9 segundos para ser renderizado. *(Isso causava instabilidade/timeout nos testes automatizados).*
* **Acessibilidade:**
  * Identificados botões e links na interface sem nomes acessíveis claros (atributos `aria-label` ou texto interno ausentes).
  * Imagens renderizadas sem o atributo descritivo `alt`.

### Ação Sugerida:
Revisar o carregamento de recursos na página principal para reduzir o tempo de LCP e adicionar atributos `alt` em todas as imagens e `aria-label` em botões/links sem texto visível para melhorar a nota de acessibilidade e a navegação por leitores de tela.


*Relatório gerado para fins de portfólio — Testes executados com auxilio de documentação e IA.*
