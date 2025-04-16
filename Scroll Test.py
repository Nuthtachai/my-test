from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException  # เพิ่มบรรทัดนี้
import time

# ระบุ path ของ chromedriver
service = Service('/usr/local/bin/chromedriver')
driver = webdriver.Chrome(service=service)

# ไปยังเว็บไซต์ที่มีเนื้อหาหลายหน้า
driver.get("https://the-internet.herokuapp.com/infinite_scroll")

# เลื่อนหน้าลงหลายครั้ง
for _ in range(4):  # เลื่อน 4 ครั้ง
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(4)  # รอ 4 วินาทีให้เนื้อหาถูกโหลด

# ตรวจสอบจำนวนของ <p> หรือองค์ประกอบที่เพิ่มขึ้น
elements = driver.find_elements(By.XPATH, "//div[@class='row']//div[@class='col-md-4']//p")
print(f"พบ {len(elements)} ข้อความ")

# รอให้เนื้อหาถูกโหลด
try:
    WebDriverWait(driver, 10).until(  # เพิ่มเวลารอเป็น 10 วินาที
        EC.presence_of_element_located((By.XPATH, "//div[@class='row']//div[@class='col-md-4']//p"))
    )
    print("✅ การทดสอบการเลื่อนหน้าสำเร็จ")
except TimeoutException:
    print("❌ การเลื่อนหน้าลงไม่ทำงานตามที่คาดหวัง")

# ปิดเบราว์เซอร์
driver.quit()
