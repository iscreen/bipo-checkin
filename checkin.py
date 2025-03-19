import time
import os
import base64
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
# options.add_argument("--headless")  # 可選：無頭模式
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    load_dotenv()

    # 1. 開啟登入頁面
    driver.get("https://ap17.bipocloud.com/SLL/Login")
    driver.add_cookie({"name": "introJs", "value": "introJs"})

    USERNAME = os.getenv('USERNAME').rstrip()
    PASSWORD = base64.standard_b64decode(os.getenv('PASSWORD')).rstrip().decode('utf-8')

    # 2. 等待登入按鈕出現（最多等 10 秒）
    wait = WebDriverWait(driver, 10)

    login_button = wait.until(
        EC.presence_of_element_located((By.ID, "btnLogin"))
    )

    # 3. 輸入帳號與密碼
    driver.find_element(By.NAME, "LoginID").send_keys(USERNAME)
    driver.find_element(By.NAME, "Password").send_keys(PASSWORD)

    # 4. 點擊登入
    login_button.click()

    # 5. 等待左側選單的 "Clock In/Out" 出現
    check_In_link = wait.until(
        EC.presence_of_element_located((By.XPATH, "//a[@url='/SLL/EMP/SSAttendance/ClockInOut']"))
    )
    check_In_link.click()

    # 6. 等待 Clock 按鈕出現並點擊
    btn_check_in = wait.until(
        EC.presence_of_element_located((By.ID, "btnClock"))
    )
    btn_check_in.click()
    print("✅ 打卡成功！")
    time.sleep(3)

except Exception as e:
    print(f"⚠️ 發生錯誤: {e}")

finally:
    driver.quit()
