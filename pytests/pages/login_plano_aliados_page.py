import time
from pytests.support.screenshot_service import ScreenshotService

class LoginPlanosAliadosPage:

    # **
    # * Mapeamento de elementos
    # **

    def field_cpf(page):
        return page.get_by_label("CPF*")

    def field_password(page):
        return page.get_by_label("Senha")

    def button_login(page):
        return page.get_by_role("button", name="Login")

    def label_user(page):
        return page.get_by_text("Emilly Elza Gomes")

    # **
    # * Métodos e Funções
    # **

    def page_planos_aliados(page):
        page.goto("https://planoaliados.com.br/portal/")
        timeout = time.time() + 15
        while time.time() < timeout:
            time.sleep(0.1)
            if LoginPlanosAliadosPage.field_cpf(page).is_visible() == True:
                break
        ScreenshotService.take_screenshot(page)
        assert page.title() == "Portal - Portal"

    def fill_login(page):
        LoginPlanosAliadosPage.field_cpf(page).fill("057.484.723-50")
        LoginPlanosAliadosPage.field_password(page).fill("654321")
        ScreenshotService.take_screenshot(page)

    def perform_login(page):
        LoginPlanosAliadosPage.button_login(page).click()
        timeout = time.time() + 15
        while time.time() < timeout:
            time.sleep(0.1)
            if LoginPlanosAliadosPage.label_user(page).is_visible() == True:
                break
        assert LoginPlanosAliadosPage.label_user(page).is_visible() == True
        ScreenshotService.take_screenshot(page)