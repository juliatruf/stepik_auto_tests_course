from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполняем обязательные поля
    input1 = browser.find_element(By.CSS_SELECTOR, ".first[required]")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, ".second[required]")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, ".third[required]")
    input3.send_keys("ivan_p@test.com")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    time.sleep(1)
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
