from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from sbis_page import SbisPage
from tensor_page import TensorPage
from errors import UrlNotCorrect, RegionNotCorrect

if __name__ == '__main__':
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    sbis_page = SbisPage(driver=driver)
    sbis_page.go_to_site()
    sbis_page.click_on_contacts()

    if sbis_page.get_region_text() != 'Пермский край':
        raise RegionNotCorrect('Регион определился неверно.')

    partners_city = sbis_page.get_partners_city_text()
    sbis_page.click_on_choice_region()

    sbis_page.click_on_kamchatka()

    partners_city_kamchatka = sbis_page.get_partners_city_text()
    new_region_text = sbis_page.get_region_text()

    if new_region_text != 'Камчатский край':
        raise RegionNotCorrect('Новый регион определился неверно.')

    title_page = sbis_page.get_title_page_text()

    if 'Камчатский' not in title_page:
        raise RegionNotCorrect('Новый регион определился неверно.')

    if 'kamchatskij-kraj' not in sbis_page.driver.current_url:
        raise RegionNotCorrect('Новый регион определился неверно.')

    if partners_city_kamchatka == partners_city:
        raise RegionNotCorrect('Новый регион определился неверно.')

    print("Новый регион определился верно.")
    driver.quit()
