
import pytest, re
from playwright.sync_api import Page, expect
from pages.fechar_popup_home import fechar_popup


def teste_exibir_detalhes(page:Page): #✅
    page.goto("https://contem1g.com.br/collections/batons/products/batom-ultra-glossy?variant=47866501038299")
    fechar_popup(page)
    expect(page.locator(".t4s-product__title").first).to_be_visible()
    

def test_comprar_produto(page:Page):
    page.goto("https://contem1g.com.br/collections/batons/products/batom-ultra-glossy?variant=47866501038299")
    fechar_popup(page)
    page.get_by_role("button", name="Adicionar ao carrinho").first.click()
    div = page.locator("div.t4s-mini_cart__items.t4s_ratioadapt.t4s-product")
    expect(div).to_be_visible()
    
def test_selecao_cor(page:Page): #✅
    page.goto("https://contem1g.com.br/collections/batons/products/batom-ultra-glossy?variant=47866501038299")
    fechar_popup(page)
    page.locator('[data-variant-id="47866501103835"]').click()
    expect(page).to_have_url("https://contem1g.com.br/collections/batons/products/batom-ultra-glossy?variant=47866501103835")
     
def test_produto_esgotado(page:Page): # se o produto voltar a ficar disponivel, este teste vai falhar
    page.goto("https://contem1g.com.br/collections/batons/products/batom-ultra-glossy?variant=47866500972763")
    fechar_popup(page)
    quantidade = page.get_by_text("Esgotado").count()
   

