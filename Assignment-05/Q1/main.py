from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# ---------------------------
# 1️⃣ Create WebDriver FIRST
# ---------------------------
options = Options()
options.add_argument("--headless")  # remove if you want to see browser
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

# ---------------------------
# 2️⃣ Open website
# ---------------------------
url = "https://www.sunbeaminfo.in/internship"
driver.get(url)

# ---------------------------
# 3️⃣ Create WebDriverWait AFTER driver
# ---------------------------
wait = WebDriverWait(driver, 15)

print("Page Title:", driver.title)

# =================================================
# 4️⃣ Internship Programs Table
# =================================================
print("\n📌 Internship Programs:")

tables = wait.until(
    EC.presence_of_all_elements_located((By.TAG_NAME, "table"))
)

program_table = tables[0]
rows = program_table.find_elements(By.TAG_NAME, "tr")

for row in rows[1:]:
    cols = row.find_elements(By.TAG_NAME, "td")
    if len(cols) >= 4:
        print(
            f"Technology: {cols[0].text}\n"
            f"Objective: {cols[1].text}\n"
            f"Prerequisite: {cols[2].text}\n"
            f"Learning: {cols[3].text}\n"
            "----------------------------"
        )

# =================================================
# 5️⃣ Internship Batch Schedule (FIXED)
# =================================================
print("\n📌 Internship Batch Schedule:")

batch_table = None

for table in tables:
    rows = table.find_elements(By.TAG_NAME, "tr")
    if len(rows) > 1:
        cols = rows[1].find_elements(By.TAG_NAME, "td")
        if len(cols) >= 7:
            batch_table = table
            break

if batch_table is None:
    print("❌ Batch schedule table not found")
else:
    batch_rows = batch_table.find_elements(By.TAG_NAME, "tr")
    for row in batch_rows[1:]:
        cols = row.find_elements(By.TAG_NAME, "td")
        if len(cols) >= 7:
            print(
                f"{cols[0].text} | {cols[1].text} | {cols[2].text} | "
                f"{cols[3].text} to {cols[4].text} | "
                f"{cols[5].text} | {cols[6].text}"
            )

# ---------------------------
# 6️⃣ Close browser
# ---------------------------
driver.quit()

