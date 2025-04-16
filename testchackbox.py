from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# ตั้งค่า path สำหรับ chromedriver
service = Service("/usr/local/bin/chromedriver")  # แก้ไขให้ตรงกับ path ของ chromedriver บนเครื่อง

# ตั้งค่า options สำหรับ Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")  # ไม่ให้เปิด UI ของ Chrome
chrome_options.add_argument("--disable-gpu")  # ใช้เมื่อไม่มี GPU หรือไม่ต้องการใช้ GPU
chrome_options.add_argument("--no-sandbox")  # สำหรับระบบที่ไม่มีการตั้งค่า sandbox

# เปิด Chrome พร้อม options และ service ที่กำหนด
driver = webdriver.Chrome(service=service, options=chrome_options)

# เปิดเว็บไซต์ Wikipedia
driver.get("https://www.wikipedia.org")

# ค้นหาคำว่า "Selenium" บน Wikipedia
search_box = driver.find_element(By.NAME, "search")
search_box.send_keys("Selenium")
search_box.send_keys(Keys.RETURN)

# ตรวจสอบว่ามีคำว่า "Selenium" ปรากฏในหน้า
time.sleep(2)  # รอหน้าโหลด
assert "Selenium" in driver.page_source, "❌ ไม่พบคำว่า 'Selenium' ในหน้า Wikipedia"

# ปิดเบราว์เซอร์
driver.quit()

print("✅ การทดสอบ Wikipedia สำเร็จ")
