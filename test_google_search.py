from allure_commons.types import Severity
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
import nidaqmx
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
    find_name.click()
    driver.close()


def test_second():
    with allure.step('Проверка аналогового входа'):
        a=0
        while a < 10:
            with nidaqmx.Task() as task:
                task.ai_channels.add_ai_voltage_chan("Dev1/ai0")
                print(task.read())
                time.sleep(0.5)
                assert task.read() > 1.5
                a += 1
                time.sleep(1)


    # Command for generate Allure report file:
    # "pytest test_google_search.py --alluredir=allure_results"
    #
    # Command for visualization Allure report in WEB page:
    # "allure serve allure_results"

def test_math_operation():
    a = 3
    b = 4
    x = a+b
    with allure.step('Проверка правильности сложения (2)'):
        assert x == 7
    with allure.step('Проверка правильности сложения'):
        assert x == 6




