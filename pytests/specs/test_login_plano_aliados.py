from pytests.support.hooks import *
from pytests.pages.login_plano_aliados_page import LoginPlanosAliadosPage
from playwright.sync_api import Page
import allure


# Descrição dos testes com pytest
@pytest.mark.test_login
def test_login(page: Page):
    with allure.step("acessar o site plano aliados"):
        LoginPlanosAliadosPage.page_planos_aliados(page)
    with allure.step("preencher o campos de login"):
        LoginPlanosAliadosPage.fill_login(page)
    with allure.step("realizar o login"):
        LoginPlanosAliadosPage.perform_login(page)