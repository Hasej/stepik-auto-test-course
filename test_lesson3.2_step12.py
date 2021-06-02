import unittest
from selenium import webdriver
import time
import pip


pip
def reg(link):
       browser = webdriver.Chrome()
       browser.get(link)

       # Ваш код, который заполняет обязательные поля
       input1 = browser.find_element_by_css_selector(".form-control.first[required]")
       input1.send_keys("Ivan")
       input2 = browser.find_element_by_css_selector(".form-control.second[required]")
       input2.send_keys("Petrov")
       input3 = browser.find_element_by_css_selector(".form-control.third[required]")
       input3.send_keys("Ivan.p@gmail.com")

       # Отправляем заполненную форму
       button = browser.find_element_by_css_selector(".btn.btn-default")
       button.click()

       # Проверяем, что смогли зарегистрироваться
       # ждем загрузки страницы
       time.sleep(1)

       return browser.find_element_by_tag_name("h1").text
class TestAbs(unittest.TestCase):
    def test_reg1(self):
        self.assertEqual(reg("http://suninjuly.github.io/registration1.html"),"Congratulations! You have successfully registered!")

    def test_reg2(self):
        self.assertEqual(reg("http://suninjuly.github.io/registration2.html"),"Congratulations! You have successfully registered!")


if __name__ == '__main__':
    unittest.main()
