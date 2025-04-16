from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time

# ระบุ path ของ chromedriver
service = Service('/usr/local/bin/chromedriver')
driver = webdriver.Chrome(service=service)

# ไปยังหน้าเว็บที่มี dropdown
driver.get("https://the-internet.herokuapp.com/dropdown")

# รอหน้าโหลดสักนิด
time.sleep(2)

# หา dropdown และเลือก option
dropdown_element = driver.find_element(By.ID, "dropdown")
select = Select(dropdown_element)

# เลือกโดยใช้ value
select.select_by_value("2")  # Option 2

# ตรวจสอบว่าเลือกถูกต้อง
selected_option = select.first_selected_option
assert selected_option.text == "Option 2", "❌ เลือก Dropdown ไม่ถูกต้อง"

print("✅ การทดสอบการเลือก Dropdown สำเร็จ")

# ปิดเบราว์เซอร์
driver.quit()
