import pages
import pytest
import re
from playwright.sync_api import Page, expect
from pages.fechar_popup_home import fechar_popup
from pages.filtros import FiltroProdutos, OrdenacaoPage


def test_aplicar_filtro_de_cor(page):
    page.goto("https://contem1g.com.br/collections/batons")
    fechar_popup(page)

    filtro = FiltroProdutos(page)
    filtro.abrir_painel_filtro()
    page.get_by_role("link",name="rosa (2)").click()
    
    page.wait_for_url(re.compile(r".*filter.*|.*color.*"), timeout=8000)

def test_aplicar_filtro_de_preco(page):
    page.goto("https://contem1g.com.br/collections/batons")
    fechar_popup(page)

    filtro = FiltroProdutos(page)
    filtro.abrir_painel_filtro()

    filtro.get_produtos_listados().first.wait_for(state="visible")
    total_produtos_antes = filtro.get_produtos_listados().count()

    
    filtro.arrastar_handle_para_valor(filtro.handle_min, valor_desejado=3000.0)
  
    
    with page.expect_response(lambda r: "collections" in r.url or "filter" in r.url, timeout=10000):
        filtro.aplicar_filtro_preco()

    filtro.get_produtos_listados().first.wait_for(state="visible", timeout=8000)
    total_produtos_depois = filtro.get_produtos_listados().count()


def test_ordenar_menor_preco(page):
    page.goto("https://contem1g.com.br/collections/batons")
    fechar_popup(page)

    ordenacao = OrdenacaoPage(page)
    ordenacao.selecionar_ordenacao("Menor preço")
    page.wait_for_url("**sort_by=price-ascending**")


def test_ordenar_maior_preco(page):
    page.goto("https://contem1g.com.br/collections/batons")
    fechar_popup(page)

    ordenacao = OrdenacaoPage(page)
    ordenacao.selecionar_ordenacao("Maior preço")
    page.wait_for_url("**sort_by=price-descending**")

def test_limpar_filtros(page):
    page.goto("https://contem1g.com.br/collections/batons")
    fechar_popup(page)

    filtro = FiltroProdutos(page)
    filtro.abrir_painel_filtro()
    page.get_by_role("link",name="rosa (2)").click()
    page.get_by_role("link", name="rosa").click() 