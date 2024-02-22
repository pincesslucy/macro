from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
from selenium.webdriver.common.alert import Alert


while True:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(3)
    driver.get("https://class.mju.ac.kr/main")

    random_time = random.uniform(4, 6)
    time.sleep(random_time)

    id = driver.find_element(By.XPATH, """//*[@id="username"]""")
    id.send_keys("학번")
    random_time = random.randint(4, 6)
    time.sleep(random_time)

    pw = driver.find_element(By.XPATH, """//*[@id="password"]""")
    pw.send_keys("비밀번호")
    random_time = random.randint(4, 6)
    time.sleep(random_time)

    rogin = driver.find_element(By.XPATH, """//*[@id="loginbuttonarea"]/button[1]""")
    rogin.click()
    random_time = random.randint(4, 6)
    time.sleep(random_time)

    try:
        while True:
            enter = driver.find_element(By.XPATH, """//*[@id="req-0106"]""")
            enter.click()
            random_time = random.random() + 0.2
            time.sleep(random_time)
            da = Alert(driver)
            da.accept()
            random_time = random.random() + 0.2
            time.sleep(random_time)
    except:
        driver.quit()
        random_time = random.randint(4, 6)
        time.sleep(random_time)
        continue