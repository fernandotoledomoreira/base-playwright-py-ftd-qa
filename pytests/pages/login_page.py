import os
from pytests.support.screenshot_service import ScreenshotService
from pytests.pages.common import Common

class LoginPage:

    # **
    # * Mapeamento de elementos
    # **

    @staticmethod
    def field_email(page):
        return page.locator("xpath=//input[@id='email']")

    @staticmethod
    def field_password(page):
        return page.locator("xpath=//input[@id='senha']")

    @staticmethod
    def button_entrar(page):
        return page.locator("xpath=//button[contains(text(),'Entrar')]")

    @staticmethod
    def element_login_sucess(page):
        return page.locator("xpath=//div[contains(text(),'Bem vindo, testudemy!')]")

    @staticmethod
    def element_login_fail(page):
        return page.locator("xpath=//div[contains(text(),'Problemas com o login do usuário')]")

    # **
    # * Métodos e Funções
    # **

    @staticmethod
    def page_sr_barriga(page):
        page.goto(f"{os.environ['uri_front_test']}")
        ScreenshotService.take_screenshot(page)
        assert page.title() == "Seu Barriga - Log in"

    @staticmethod
    def fill_login(page):
        LoginPage.field_email(page).fill("test@test")
        LoginPage.field_password(page).fill("123")
        ScreenshotService.take_screenshot(page)

    @staticmethod
    def fill_login_invalid(page, field, value):
        if field == "email":
            value = Common.values_change(value)
            LoginPage.field_email(page).fill(value)
            LoginPage.field_password(page).fill("123")
        else:
            value = Common.values_change(value)
            LoginPage.field_email(page).fill("test@test")
            LoginPage.field_password(page).fill(value)
        ScreenshotService.take_screenshot(page)

    @staticmethod
    def perform_login(page):
        LoginPage.button_entrar(page).click()
        elemente = LoginPage.element_login_sucess(page)
        assert elemente.text_content() == "Bem vindo, testudemy!"
        ScreenshotService.take_screenshot(page)

    @staticmethod
    def perform_login_invalid(page, field):
        LoginPage.button_entrar(page).click()
        if field == "email":
            assert page.is_visible("body > div.alert.alert-success") == False
        else:
            elemente = LoginPage.element_login_fail(page)
            assert elemente.text_content() == "Problemas com o login do usuário"
        ScreenshotService.take_screenshot(page)