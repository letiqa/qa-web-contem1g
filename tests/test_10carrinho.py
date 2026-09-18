import pytest, re
from playwright.sync_api import Page, expect
from pages.fechar_popup_home import fechar_popup


def test_adicionar_produto_carrinho(page: Page):
    page.goto("https://contem1g.com.br/collections/batons/products/batom-ultra-glossy?variant=47866501103835")
    fechar_popup(page)
    page.get_by_role("button", name="Adicionar ao carrinho").first.click()
    expect(page.locator("span[data-cart-count]")).to_contain_text("1")
    
def test_aumentar_quantidade_no_carrinho(page:Page):
    page.goto("https://contem1g.com.br/collections/batons/products/batom-ultra-glossy?variant=47866501103835")
    fechar_popup(page)
    page.get_by_role("button", name="Adicionar ao carrinho").first.click()
    expect(page.locator("span[data-cart-count]")).to_contain_text("1")
    page.get_by_label("Fechar carrinho").click() 
    page.get_by_role("button", name="Adicionar ao carrinho").first.click()
    expect(page.locator("span[data-cart-count]")).to_contain_text("2")

def test_excluir_do_carrinho(page: Page):
    page.goto("https://contem1g.com.br/collections/batons/products/batom-ultra-glossy?variant=47866501103835")
    fechar_popup(page)
    page.get_by_role("button", name="Adicionar ao carrinho").first.click()
    page.locator(".t4s-quantity-cart-item button[data-decrease-qty]").click()
    expect(page.get_by_text("O carrinho está vazio").first).to_be_visible()


    