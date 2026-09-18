import pytest
from playwright.sync_api import Page, expect
from pages.fechar_popup_home import fechar_popup


def test_galeria_imagens(page: Page):
    """
    Teste básico: verifica se a imagem principal da galeria muda ao navegar.
    
    A galeria usa Flickity slider (tema T4S). A imagem visível é a que está no 
    t4s-product__media-item com classe 'is-selected' (ou sem 'is--media-hide').
    """
    page.goto("https://contem1g.com.br/collections/batons/products/batom-ultra-glossy?variant=47866501038299")
    fechar_popup(page)

    # Função helper para obter a imagem visível atual
    def get_imagem_visivel_data_master():
        item_selecionado = page.locator('.t4s-product__media-item.is-selected').first
        if item_selecionado.count() == 0:
            item_selecionado = page.locator('.t4s-product__media-item:not(.is--media-hide)').first
        img = item_selecionado.locator('img[alt="Batom Ultra Glossy"]').first
        expect(img).to_have_attribute("data-master", timeout=5000)
        return img.get_attribute("data-master")

    # Captura imagem inicial
    imagem_inicial = get_imagem_visivel_data_master()
    assert imagem_inicial, "Deve haver uma imagem visível na galeria"

    # Clica no botão Next da galeria
    botao_next = page.locator('button[aria-label="Next"]').first
    expect(botao_next).to_be_visible()
    botao_next.click()
    
    # Aguarda transição do slider
    page.wait_for_timeout(1500)

    # Verifica se a imagem mudou
    imagem_nova = get_imagem_visivel_data_master()
    assert imagem_nova != imagem_inicial, "A imagem da galeria deve mudar ao clicar Next"


def test_galeria_navegacao_completa_previous_next(page: Page):
    """
    Verifica navegação completa Previous/Next na galeria Flickity.
    """
    page.goto("https://contem1g.com.br/collections/batons/products/batom-ultra-glossy?variant=47866501038299")
    fechar_popup(page)

    def get_imagem_visivel():
        item = page.locator('.t4s-product__media-item.is-selected').first
        if item.count() == 0:
            item = page.locator('.t4s-product__media-item:not(.is--media-hide)').first
        return item.locator('img[alt="Batom Ultra Glossy"]').first.get_attribute("data-master")

    inicial = get_imagem_visivel()
    
    # Next
    page.locator('button[aria-label="Next"]').first.click()
    page.wait_for_timeout(1500)
    depois_next = get_imagem_visivel()
    assert depois_next != inicial, "Next deve trocar a imagem"

    # Previous
    page.locator('button[aria-label="Previous"]').first.click()
    page.wait_for_timeout(1500)
    depois_prev = get_imagem_visivel()
    assert depois_prev != depois_next, "Previous deve trocar a imagem"
    # Opcional: verificar se voltou ao original
    # assert depois_prev == inicial, "Previous deve voltar à imagem original"


def test_galeria_tem_multiplas_imagens_unicas(page: Page):
    """
    Verifica que a galeria contém múltiplas imagens distintas (não é imagem única).
    """
    page.goto("https://contem1g.com.br/collections/batons/products/batom-ultra-glossy?variant=47866501038299")
    fechar_popup(page)

    def get_imagem_visivel():
        item = page.locator('.t4s-product__media-item.is-selected').first
        if item.count() == 0:
            item = page.locator('.t4s-product__media-item:not(.is--media-hide)').first
        return item.locator('img[alt="Batom Ultra Glossy"]').first.get_attribute("data-master")

    botao_next = page.locator('button[aria-label="Next"]').first
    expect(botao_next).to_be_visible()

    imagens_unicas = set()
    
    # Navega pela galeria coletando imagens únicas
    for _ in range(15):  # Máximo 15 cliques (galeria tem 7 imagens)
        img_atual = get_imagem_visivel()
        imagens_unicas.add(img_atual)
        
        botao_next.click()
        page.wait_for_timeout(1000)
        
        # Para se completou o ciclo
        if get_imagem_visivel() == list(imagens_unicas)[0] and len(imagens_unicas) > 1:
            break

    assert len(imagens_unicas) >= 2, \
        f"Galeria deve ter múltiplas imagens, encontrou apenas {len(imagens_unicas)} única(s)"