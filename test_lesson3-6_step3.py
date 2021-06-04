from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math
import pytest

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

lessons = [
    ("236895"),
    ("236896"),
    ("236897"),
    ("236898"),
    ("236899"),
    ("236903"),
    ("236904"),
    ("236905")
]
    @pytest.mark.parametrize("lesson", lessons)
    def test_get_correct_answer (browser, lesson):
        link = f"https://stepik.org/lesson/{}/step/1".format(code)
        browser.get(link)


        answer = math.log(int(time.time()))

        input1 = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.TAG_NAME, 'textarea'))
        )
        input1.send_keys(answer)

        button1 = browser.find_element_by_css_selector(.sumbit-submission)
        button1.click()

        message = WebDriverWait(browser, 5).until(
        EC.text_to_be_present_in_element(By.CSS_SELECTOR, '.smart-hints__hint')
        )

        assert "Correct!" in message.text , "should be \"Correct!\" instead {message.text}"




