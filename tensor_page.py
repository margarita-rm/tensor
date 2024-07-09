from base_app import BasePage
from selenium.webdriver.common.by import By


class TensorLocators:
    LOCATOR_ABOUT_LINK = (By.CSS_SELECTOR, 'a[href="/about"]')
    LOCATOR_BLOCK_IMAGES = (By.CLASS_NAME, 'tensor_ru-About__block3-image-filter')


class TensorPage(BasePage):

    def click_on_about(self):
        return self.find_element(TensorLocators.LOCATOR_ABOUT_LINK).click()

    def get_sizes_images(self) -> list[dict]:
        images = self.find_elements(TensorLocators.LOCATOR_BLOCK_IMAGES)
        return [image.size for image in images]
