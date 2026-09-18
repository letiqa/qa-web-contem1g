# pyrefly: ignore [missing-import]
from playwright.sync_api import Page, expect
from pages.fechar_popup_home import fechar_popup


class itens_menu_sub:   
    def __init__(self, page: Page):
        self.page = page

    def navegar_categoria_subcategoria(self, categoria: str, subcategoria: str, url_esperada: str):
        self.page.goto("https://contem1g.com.br/", timeout=15000)
        fechar_popup(self.page)
        menu_item = self.page.get_by_role("link", name=categoria, exact=True).first
        expect(menu_item).to_be_visible()
        menu_item.hover()
        self.page.wait_for_timeout(500)
        self.page.get_by_role("link", name=subcategoria, exact=True).click()
        expect(self.page).to_have_url(url_esperada)




class itens_menu_categoria:   
    def __init__(self, page: Page):
        self.page = page

    def navegar_categoria(self, categoria: str, url_esperada: str):
        self.page.goto("https://contem1g.com.br/", timeout=15000)
        fechar_popup(self.page)
        menu_item = self.page.get_by_role("link", name=categoria, exact=True).click()
        self.page.wait_for_timeout(500)
        expect(self.page).to_have_url(url_esperada)