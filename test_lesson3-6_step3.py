from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math
import pytest
import unittest

@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    time.sleep(5)
    browser.quit()

class TestAnswer():
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
    def test_get_correct_answer(self, browser, lesson, result):
        link = "https://stepik.org/lesson/{}/step/1".format(lesson)
        browser.get(link)


        answer = str(math.log(int(time.time())))

        input1 = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.TAG_NAME, 'textarea'))
        )
        input1.send_keys(answer)

        button1 = browser.find_element_by_css_selector(".submit-submission")
        button1.click()

        time.sleep(3)

        message = browser.find_element_by_css_selector(".smart-hints__hint")

        if message.text != "Correct!":
            self.result += message.text
            print(self.lessons)

        assert message.text == "Correct!", f"should be \"Correct!\" instead \"{message.text}\""

if __name__ == "__main__":
    test_get_correct_answer()
    print(self.result)







