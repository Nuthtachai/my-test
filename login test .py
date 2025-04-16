from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

# ตั้งค่าชื่อและรหัสผ่านแบบสุ่ม
username = f"testuser{random.randint(1000,9999)}"
password = "testpass123"

# เริ่มต้น WebDriver
service = Service('/usr/local/bin/chromedriver')
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://www.demoblaze.com/")
time.sleep(2)

### 🔹 ขั้นตอนที่ 1: สมัครสมาชิก
print("🔸 เริ่มการทดสอบสมัครสมาชิก...")
signup_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "signin2"))
)
driver.execute_script("arguments[0].scrollIntoView(true);", signup_button)
signup_button.click()
time.sleep(2)

# ป้อนชื่อผู้ใช้และรหัสผ่าน
driver.find_element(By.ID, "sign-username").send_keys(username)
driver.find_element(By.ID, "sign-password").send_keys(password)
driver.find_element(By.XPATH, "//button[text()='Sign up']").click()
time.sleep(3)

# รับ Alert การสมัคร
try:
    alert = driver.switch_to.alert
    print(f"📣 Alert: {alert.text}")
    alert.accept()
except:
    print("⚠️ ไม่มี alert แสดงหลังสมัคร")

time.sleep(2)

### 🔹 ขั้นตอนที่ 2: ล็อกอินด้วยบัญชีที่เพิ่งสมัคร
print("🔸 เริ่มการทดสอบล็อกอิน...")

# คลิกปุ่ม Log in
login_button = driver.find_element(By.ID, "login2")
driver.execute_script("arguments[0].scrollIntoView(true);", login_button)
login_button.click()
time.sleep(2)

# ป้อนชื่อผู้ใช้และรหัสผ่าน
driver.find_element(By.ID, "loginusername").send_keys(username)
driver.find_element(By.ID, "loginpassword").send_keys(password)
driver.find_element(By.XPATH, "//button[text()='Log in']").click()
time.sleep(3)

# ตรวจสอบว่าเข้าสู่ระบบสำเร็จหรือไม่
try:
    welcome_text = driver.find_element(By.ID, "nameofuser").text
    if username in welcome_text:
        print(f"✅ ล็อกอินสำเร็จ: {welcome_text}")
    else:
        print("❌ เข้าสู่ระบบไม่สำเร็จ (ชื่อไม่ตรง)")
except:
    print("❌ ไม่สามารถเข้าสู่ระบบได้")

# ปิดเบราว์เซอร์
driver.quit()
