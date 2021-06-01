from selenium import webdriver
import time
import os 


try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')


    input1 = browser.find_element_by_css_selector(".form-control[name='firstname']")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector(".form-control[name='lastname']")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector(".form-control[name='email']")
    input3.send_keys("Ivan.p@gmail.com")
    input4 = browser.find_element_by_id("file")
    input4.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector(".btn.btn-primary")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

    


    
