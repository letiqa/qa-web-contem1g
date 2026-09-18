# pyrefly: ignore [missing-import]
import pytest
# pyrefly: ignore [missing-import]
from playwright.sync_api import Page, expect
# pyrefly: ignore [missing-import]
from pages.fechar_popup_home import fechar_popup

#testa se os botões dos carrosseis na home estão funcionando

def test_2botoescarrosseis(page: Page):
    page.goto("https://contem1g.com.br/", timeout=15000)
    fechar_popup(page)
   

