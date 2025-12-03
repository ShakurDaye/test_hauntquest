from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Start browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

# 1. Go to website
driver.get("https://ryanzomparelli.github.io/Oct-Code-Jam-2025/index.html")

# 2. Boolean check that site loaded
site_loaded = "HauntQuest" in driver.title
print("Site loaded:", site_loaded)
time.sleep(3)

# 3. Click the "Future Events" tab
future_events_tab = driver.find_element(By.XPATH, "//button[normalize-space()='Future Events']")
future_events_tab.click()
time.sleep(2)
print("Clicked Future Events tab ✔")

#4. Click the Home Tab
home_tab = driver.find_element(By.XPATH, "//a[normalize-space()='Home']")
home_tab.click()
print("Home tab is Clicked")
time.sleep(3)

#5. Click the "Search Events Tab"
search_events_tab = driver.find_element(By.XPATH, "//input[@name='event-filter']")
search_events_tab.click()
print("Search Tab is clicked")
time.sleep(3)

#6 Type "HI" into the search input field
search_box = driver.find_element(By.NAME, "event-filter")
search_box.send_keys("HI")
print('Typed "HI" into the search box')
time.sleep(3)
driver.quit()


