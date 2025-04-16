import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# เริ่มจับเวลา
start_time = time.time()

# เรียกใช้งาน WebDriver
service = Service("/usr/local/bin/chromedriver")  # เปลี่ยน path ตามเครื่องคุณ
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # เปิดแบบไม่แสดงเบราว์เซอร์

driver = webdriver.Chrome(service=service, options=options)

# เข้าเว็บไซต์
driver.get("https://www.nekopost.net/explore?cate=yuri")

# รอให้หน้าเว็บโหลดเสร็จ (ตรวจดูว่า element สำคัญแสดงแล้ว)
driver.implicitly_wait(10)

# จับเวลาเสร็จ
end_time = time.time()
load_time = end_time - start_time

print(f"⏱️ ใช้เวลาโหลดหน้า https://www.nekopost.net/explore?cate=yuri ทั้งหมด: {load_time:.2f} วินาที")

# ปิดเบราว์เซอร์
driver.quit()
