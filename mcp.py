import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Google Sheets authentication
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name("C:\\Users\\Harsha PC\\Downloads\\client_secret_292138168979-55bvms95js7uauie7mi289f5rp3rjepn.apps.googleusercontent.com.json", scope)
client = gspread.authorize(credentials)

# Open Google Sheet
sheet = client.open("C:\\Users\\Harsha PC\\Downloads\\twitter_dataset.xlsx").sheet1

# Fetch all data
data = sheet.get_all_records()
print(data)


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import chromedriver_autoinstaller

# Auto-install the correct ChromeDriver version
chromedriver_autoinstaller.install()

# Launch browser
driver = webdriver.Chrome()
driver.get("https://twitter.com/login")

# Login to Twitter
username = driver.find_element(By.NAME, "session[username_or_email]")
password = driver.find_element(By.NAME, "session[password]")

username.send_keys("your_username")
password.send_keys("your_password")
password.send_keys(Keys.RETURN)

time.sleep(5)

# Post a tweet
tweet_box = driver.find_element(By.XPATH, "//div[@aria-label='Tweet text']")
tweet_box.send_keys("Hello from Python!")
tweet_button = driver.find_element(By.XPATH, "//div[@data-testid='tweetButtonInline']")
tweet_button.click()

time.sleep(5)
driver.quit()


sheet.update_cell(row, col, "Posted")
