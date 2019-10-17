from allure_commons.types import Severity
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
import time
import allure

@allure.title('Результат поиска')
@allure.severity(Severity.BLOCKER)
def test_google_search():

    driver = WebDriver(executable_path='C:\dpe\Chromdriver\chromedriver.exe')
    with allure.step('Открывем страницу поиска'):
        driver.get('https://www.google.com/')  #Open Google.com in Google Chrome browser
    find_serch = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input') #Search for input on a web page
    with allure.step('Вводим название сайта'):
        find_serch.send_keys('renarosh')
        time.sleep(2)
    with allure.step('Поиск кнопки Ввод'):
        find_name = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[2]/div[2]/div[2]/center/input[1]')
        print("Check")
    find_name.click()


