from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# ระบุ path ที่ถูกต้องของ chromedriver
service = Service('/usr/local/bin/chromedriver')

# ใช้ service ตอนสร้าง driver
driver = webdriver.Chrome(service=service)

# เปิดเว็บ Google
driver.get("https://www.google.com")

# ค้นหาคำว่า "Selenium Python"
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium Python")
search_box.send_keys(Keys.RETURN)

# รอให้ผลการค้นหาขึ้น
time.sleep(2)

# ตรวจสอบว่ามีคำว่า "Selenium" อยู่ในหน้าผลลัพธ์
assert "Selenium" in driver.page_source

# ปิดเบราว์เซอร์
driver.quit()
