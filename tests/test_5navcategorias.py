# pyrefly: ignore [missing-import]
import pytest
# pyrefly: ignore [missing-import]
from playwright.sync_api import Page, expect
# pyrefly: ignore [missing-import]
from pages.fechar_popup_home import fechar_popup
# pyrefly: ignore [missing-import]
from pages.itens_menu import itens_menu_categoria

# Este teste verifica a navegação pelas categorias de produto do site e suas subcategorias

def test_navegacao_olhos(page: Page):
    menu = itens_menu_categoria(page)
    menu.navegar_categoria(
        categoria="Olhos",
        url_esperada="https://contem1g.com.br/collections/olhos",
    )

def test_navegacao_face(page: Page):
    menu = itens_menu_categoria(page)
    menu.navegar_categoria(
        categoria="Face",
        url_esperada="https://contem1g.com.br/collections/face",
    )

def test_navegacao_labios(page: Page):
    menu = itens_menu_categoria(page)
    menu.navegar_categoria(
        categoria="Lábios",
        url_esperada="https://contem1g.com.br/collections/labios",
    ) 
    
def test_navegacao_fragrancia(page: Page):
    menu = itens_menu_categoria(page)
    menu.navegar_categoria(
        categoria="Fragrância",
        url_esperada="https://contem1g.com.br/collections/pink",
    )
    
def test_navegacao_looks(page: Page):
    menu = itens_menu_categoria(page)
    menu.navegar_categoria(
        categoria="Looks",
        url_esperada="https://contem1g.com.br/collections/looks",
    )

def test_navegacao_kits(page: Page):
    menu = itens_menu_categoria(page)
    menu.navegar_categoria(
        categoria="Kits",
        url_esperada="https://contem1g.com.br/collections/kits",
    )

def test_navegacao_ofertas(page: Page):
    menu = itens_menu_categoria(page)
    menu.navegar_categoria(
        categoria="Ofertas",
        url_esperada="https://contem1g.com.br/collections/ofertas",
    )