# pyrefly: ignore [missing-import]
import pytest 
# pyrefly: ignore [missing-import]
from playwright.sync_api import Page, expect
def test_1loadhome(page: Page):
   page.goto("https://contem1g.com.br/") 
   page.locator(" t4s-header__logo t4s-lh-1") 
   # localiza a header com o logo da marca, localizar pelo nome da imagem mostrava 3 arquivos com o mesmo nome, então localizei pela classe da header
   