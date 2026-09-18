# pyrefly: ignore [missing-import]
from playwright.sync_api import Page, expect


class FiltroProdutos:
    def __init__(self, page: Page):
        self.page = page
        self.botao_filtrar = page.get_by_role("button", name="Show filters")

        # --- price slider (noUiSlider confirmado via DOM real) ---
        self.track_slider = page.locator(".noUi-target").first
        self.handle_min = page.locator(".noUi-handle-lower")
        self.handle_max = page.locator(".noUi-handle-upper")
        # botão que aplica o filtro de preço após mover o slider (fica oculto até então)
        self.botao_aplicar_preco = page.get_by_role("button", name="Filtrar")

    def abrir_painel_filtro(self):
        self.botao_filtrar.click()
        # espera de verdade: garante que o painel terminou de abrir/animar
        # antes de qualquer interação com os elementos internos (ex: slider)
        self.track_slider.wait_for(state="visible", timeout=5000)


    def get_limites_slider(self, handle) -> tuple[float, float]:
        """Lê o min/max configurado no slider (aria-valuemin / aria-valuemax)."""
        minimo = float(handle.get_attribute("aria-valuemin"))
        maximo = float(handle.get_attribute("aria-valuemax"))
        return minimo, maximo

    def arrastar_handle_para_valor(self, handle, valor_desejado: float):
        """
        Arrasta um handle até um valor de preço específico (ex: 30.0 = R$30,00),
        calculando o percentual do track com base no min/max real do slider.
        """
        minimo, maximo = self.get_limites_slider(handle)
        percentual_destino = (valor_desejado - minimo) / (maximo - minimo)
        self.arrastar_handle(handle, percentual_destino)

    def arrastar_handle(self, handle, percentual_destino: float):
        """
        Arrasta um handle até uma posição relativa do track (0.0 a 1.0).
        Ex: 0.5 = arrasta até o meio do slider.
        """
        # mouse.move/down/up não fazem auto-scroll como o .click() faz,
        # então garantimos manualmente que o elemento está visível na tela
        handle.scroll_into_view_if_needed()
        self.track_slider.scroll_into_view_if_needed()

        track_box = self.track_slider.bounding_box()
        handle_box = handle.bounding_box()

        if track_box is None or handle_box is None:
            raise ValueError("Não foi possível obter a posição do slider/handle na tela")

        origem_x = handle_box["x"] + handle_box["width"] / 2
        origem_y = handle_box["y"] + handle_box["height"] / 2

        destino_x = track_box["x"] + (track_box["width"] * percentual_destino)

        try:
            self.page.mouse.move(origem_x, origem_y)
            self.page.mouse.down()
            self.page.wait_for_timeout(100)  # dá tempo do slider registrar o início do drag

            passos = 15
            for i in range(1, passos + 1):
                x_intermediario = origem_x + (destino_x - origem_x) * (i / passos)
                self.page.mouse.move(x_intermediario, origem_y, steps=1)
                self.page.wait_for_timeout(20)  # pequeno delay entre movimentos
        finally:
          
            self.page.mouse.up()

    def aplicar_filtro_preco(self):
        self.botao_aplicar_preco.wait_for(state="visible", timeout=5000)
        self.botao_aplicar_preco.click()

    def get_produtos_listados(self):
    
        return self.page.locator(".t4s_box_pr_grid .t4s-product:visible")

class OrdenacaoPage:
    def __init__(self, page):
        self.page = page
        self.botao_ordenar = page.locator('[data-id="t4s__sortby"]')

    def abrir_dropdown_ordenacao(self):
        self.botao_ordenar.click()

    def selecionar_ordenacao(self, opcao: str):
        self.abrir_dropdown_ordenacao()
        # ajustar o seletor da opção assim que soubermos o HTML real
        self.page.get_by_text(opcao, exact=True).click()
