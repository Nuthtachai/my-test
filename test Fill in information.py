from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# ระบุ path ไปยัง chromedriver
service = Service('/usr/local/bin/chromedriver')
driver = webdriver.Chrome(service=service)

# เปิดหน้าฟอร์ม
driver.get("https://formy-project.herokuapp.com/form")

# กรอกข้อมูลในฟอร์ม
driver.find_element(By.ID, "first-name").send_keys("Ines")
driver.find_element(By.ID, "last-name").send_keys("Tester")
driver.find_element(By.ID, "job-title").send_keys("QA Engineer")
driver.find_element(By.ID, "radio-button-2").click()  # College
driver.find_element(By.ID, "checkbox-2").click()      # Female

# ✅ ใช้ class หรือ xpath เพื่อคลิกปุ่ม submit
driver.find_element(By.CLASS_NAME, "btn").click()

# รอให้หน้าโหลด
time.sleep(2)

# ตรวจสอบข้อความหลังส่งฟอร์ม
assert "Thanks for submitting your form" in driver.page_source

# ปิดเบราว์เซอร์
driver.quit()
