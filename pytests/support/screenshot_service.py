import allure
from pytests.support.hooks import *

class ScreenshotService:

    def take_screenshot(page):
        page.screenshot(path=PATH_SCREENSHOT)
        allure.attach.file(PATH_SCREENSHOT, attachment_type=allure.attachment_type.PNG)