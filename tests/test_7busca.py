# pyrefly: ignore [missing-import]
import pytest
# pyrefly: ignore [missing-import]
import re
from playwright.sync_api import Page, expect
# pyrefly: ignore [missing-import]

from pages.fechar_popup_home import fechar_popup

#testa buscas por termo valido

def test_termo_valido(page: Page):
    page.goto("https://contem1g.com.br/", timeout=15000)
    fechar_popup(page)
    page.locator(".t4s-site-nav__icon > .t4s-pr").first.click()
    page.get_by_placeholder("Buscar").fill("batom")
    page.locator(".t4s-mini-search__submit").click() 
    expect(page).to_have_url(re.compile(r"q=batom"))

    #verifica se a mensagem de "resultados de pesquisa" aparece
    expect(page.get_by_text(re.compile(r"\d+ resultados da pesquisa"))).to_be_visible()

    # espera pelo menos 1 produto aparecer no grid
    produtos = page.locator(".t4s-full-width-link")  
    expect(produtos.first).to_be_visible()

    
    # O teste automatizado valida que resultados existem e que a contagem é reportada corretamente. 
    # A validação de relevância semântica dos resultados (ex: sinônimos, categorias relacionadas) 
    # requer revisão manual/exploratória, já que depende de regras de negócio do algoritmo de busca.

    