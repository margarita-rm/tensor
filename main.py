from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from sbis_page import SbisPage
from tensor_page import TensorPage
from errors import UrlNotCorrect

if __name__ == '__main__':
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    sbis_page = SbisPage(driver=driver)
    sbis_page.go_to_site()
    sbis_page.click_on_contacts()
    tensor_handle = sbis_page.click_on_tensor()

    driver.switch_to.window(tensor_handle)

    tensor_page = TensorPage(driver=driver)
    tensor_page.click_on_about()

    if tensor_page.driver.current_url != 'https://tensor.ru/about':
        raise UrlNotCorrect('Ссылка неверная.')

    images = tensor_page.get_sizes_images()
    if all(attr == images[0] for attr in images):
        print("Все словари равны.")
    else:
        print("Словари не равны.")

    driver.quit()
