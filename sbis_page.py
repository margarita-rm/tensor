from functools import lru_cache

from base_app import BasePage
from selenium.webdriver.common.by import By


class SbisLocators:
    LOCATOR_CONTACTS_LINK = (By.CSS_SELECTOR, 'a[href="/contacts"]')
    LOCATOR_TENSOR_LINK = (By.CSS_SELECTOR, 'a[href="https://tensor.ru/"]')
    LOCATOR_TENSOR_ABOUT_LINK = (By.CSS_SELECTOR, 'a[href="/about"]')
    LOCATOR_CURRENT_REGION = (By.CLASS_NAME, 'sbis_ru-Region-Chooser__text')
    LOCATOR_PARTNERS_CITY = (By.ID, 'city-id-2')
    LOCATOR_KAMCHATKA_LINK = (By.XPATH, "//span[@title='Камчатский край']")
    LOCATOR_TITLE_PAGE = (By.TAG_NAME, 'title')


class SbisPage(BasePage):

    def click_on_contacts(self):
        return self.find_element(SbisLocators.LOCATOR_CONTACTS_LINK).click()

    def click_on_tensor(self):
        tensor_link = self.find_element(SbisLocators.LOCATOR_TENSOR_LINK)
        tensor_link.click()
        return self.driver.window_handles[1]

    def click_on_about_block(self):
        return self.find_element(SbisLocators.LOCATOR_TENSOR_ABOUT_LINK).click()

    @property
    @lru_cache
    def get_element_region(self):
        return self.find_element(SbisLocators.LOCATOR_CURRENT_REGION)

    def get_region_text(self):
        return self.get_element_region.text

    def click_on_choice_region(self):
        return self.get_element_region.click()

    def get_partners_city_text(self):
        return self.find_element(SbisLocators.LOCATOR_PARTNERS_CITY).text

    def click_on_kamchatka(self):
        return self.find_element(SbisLocators.LOCATOR_KAMCHATKA_LINK).click()

    def get_title_page_text(self):
        return self.driver.title
