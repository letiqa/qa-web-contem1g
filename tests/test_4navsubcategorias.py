# pyrefly: ignore [missing-import]
import pytest
# pyrefly: ignore [missing-import]
from playwright.sync_api import Page, expect
# pyrefly: ignore [missing-import]
from pages.fechar_popup_home import fechar_popup
# pyrefly: ignore [missing-import]
from pages.itens_menu import itens_menu_sub

# Este teste verifica se o submenu das categorias do site carregam

def test_navegacao_olhos(page: Page):
    menu = itens_menu_sub(page)
    menu.navegar_categoria_subcategoria(
        categoria="Olhos",
        subcategoria="Lápis e Lapiseiras de Olhos",
        url_esperada="https://contem1g.com.br/collections/lapis-de-olhos",
    )


def test_navegacao_face(page: Page):
    menu = itens_menu_sub(page)
    menu.navegar_categoria_subcategoria(
        categoria="Face",
        subcategoria="Bases",
        url_esperada="https://contem1g.com.br/collections/bases",
         )



def test_navegacao_labios(page: Page):
    menu = itens_menu_sub(page)
    menu.navegar_categoria_subcategoria(
        categoria="Lábios",
        subcategoria="Gloss",
        url_esperada="https://contem1g.com.br/collections/gloss",
         )

