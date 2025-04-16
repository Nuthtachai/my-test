from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# กำหนด path ไปยัง chromedriver (เปลี่ยน path หากจำเป็น)
service = Service('/usr/local/bin/chromedriver')
driver = webdriver.Chrome(service=service)

# เปิดเว็บไซต์
driver.get("https://demoqa.com/books")

# รอให้ช่องค้นหาแสดงก่อนเริ่มทำงาน
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "searchBox"))
)

# รายการคำค้นที่ต้องการทดสอบ
keywords = ["Design", "JavaScript", "Git", "Python", "NoBookShouldMatchThis"]

for keyword in keywords:
    search_box = driver.find_element(By.ID, "searchBox")
    search_box.clear()  # ล้างข้อความเก่าก่อนพิมพ์ใหม่
    search_box.send_keys(keyword)

    # รอให้ผลการค้นหาปรากฏ
    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "action-buttons"))
        )
        books = driver.find_elements(By.CLASS_NAME, "action-buttons")
        if books:
            print(f"✅ พบผลลัพธ์สำหรับคำว่า '{keyword}' จำนวน {len(books)} รายการ")
        else:
            print(f"❌ ไม่พบผลลัพธ์สำหรับคำว่า '{keyword}'")
    except:
        print(f"❌ ไม่พบผลลัพธ์สำหรับคำว่า '{keyword}' (timeout)")

# ปิด browser เมื่อเสร็จ
driver.quit()
