# pyrefly: ignore [missing-import]
import pytest
# pyrefly: ignore [missing-import]
from playwright.sync_api import Page, expect
# pyrefly: ignore [missing-import]
from pages.fechar_popup_home import fechar_popup

# Este teste verifica se todos os links do footer estao funcionando, e se levam para o local correto

def test_links_footer(page: Page):
    page.goto("https://contem1g.com.br/", timeout=15000)
    fechar_popup(page) 
    page.get_by_text("Política de Devolução").click()
    expect(page).to_have_url("https://contem1g.com.br/policies/refund-policy")
    
    page.goto("https://contem1g.com.br/", timeout=15000)
    fechar_popup(page)
    page.get_by_text("Política de Privacidade").click()
    expect(page).to_have_url("https://contem1g.com.br/policies/privacy-policy")

    
    page.goto("https://contem1g.com.br/", timeout=15000)
    fechar_popup(page)
    page.get_by_text("Termos e Condições de Uso").click()
    expect(page).to_have_url("https://contem1g.com.br/policies/terms-of-service")

    
    page.goto("https://contem1g.com.br/", timeout=15000)
    fechar_popup(page)
    page.get_by_text("Mapa do site").click()
    expect(page).to_have_url("https://contem1g.com.br/a/sitemap-tools/sitemap")

    
    page.goto("https://contem1g.com.br/", timeout=15000)
    fechar_popup(page)
    page.get_by_text("Sobre a Contém1g").click()
    expect(page).to_have_url("https://contem1g.com.br/pages/sobre-nos")

    
    page.goto("https://contem1g.com.br/", timeout=15000)
    fechar_popup(page)
    page.get_by_text("Dúvidas").click()
    expect(page).to_have_url("https://contem1g.com.br/apps/frequently-asked-questions?faq-section-id=126268&faq-article-id=568000")

    
    page.goto("https://contem1g.com.br/", timeout=15000)
    fechar_popup(page)
    page.get_by_text("Trabalhe conosco").click()
    expect(page).to_have_url("https://sallve.inhire.app/vagas")

    
    page.goto("https://contem1g.com.br/", timeout=15000)
    fechar_popup(page)
    page.get_by_text("Onde encontrar").click()
    expect(page).to_have_url("https://contem1g.com.br/pages/onde-encontrar")

    
    page.goto("https://contem1g.com.br/", timeout=15000)
    fechar_popup(page)
    page.get_by_text("Resenhas").click()
    expect(page).to_have_url("https://contem1g.com.br/pages/resenhas")
    
    page.goto("https://contem1g.com.br/", timeout=15000)
    fechar_popup(page)
    expect(page.get_by_role("link", name="faleconosco@contem1g.com.br")).to_have_attribute("href", "mailto:faleconosco@contem1g.com.br")

def test_redes_sociais(page: Page): 
    page.goto("https://contem1g.com.br/", timeout=15000)
    fechar_popup(page)
    with page.context.expect_page() as new_page_info:
        page.locator("a.facebook").click()
    new_page = new_page_info.value
    new_page.wait_for_load_state()
    expect(new_page).to_have_url("https://www.facebook.com/contem1g")
    new_page.close()

    
    page.goto("https://contem1g.com.br/", timeout=15000)
    fechar_popup(page)
    with page.context.expect_page() as new_page_info:
        page.locator("a.instagram").click()
    new_page = new_page_info.value
    new_page.wait_for_load_state()
    expect(new_page).to_have_url("https://www.instagram.com/contem1g.oficial/")
    new_page.close()