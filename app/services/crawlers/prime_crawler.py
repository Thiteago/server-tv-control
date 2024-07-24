from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import time
import os

class PrimeCrawler:
  def __init__(self, driver):
    self.driver = driver
    load_dotenv()

  def login(self):
    time.sleep(5)
    
    sign_in_button = self.driver.find_element(By.XPATH, "//a[contains(@href, '/auth-redirect/')]")
    new_url = sign_in_button.get_attribute('href')
    print(new_url)
    self.driver.get(new_url)
    time.sleep(5)

    WebDriverWait(self.driver, 10).until(
      EC.presence_of_element_located((By.ID, 'ap_email'))
    )

    email_input = self.driver.find_element(By.ID, 'ap_email')
    email = os.getenv('PRIME_VIDEO_EMAIL')
    time.sleep(5)
    email_input.send_keys(email)
    continue_button = self.driver.find_element(By.CSS_SELECTOR, 'input[id="continue"]')
    continue_button.click()
    time.sleep(5)
    password_input = self.driver.find_element(By.CSS_SELECTOR, 'input[id="ap_password"]')
    password_input.send_keys(os.getenv('PRIME_VIDEO_PASSWORD'))
    login_button = self.driver.find_element(By.CSS_SELECTOR, 'input[id="signInSubmit"]')
    login_button.click()
    time.sleep(5)

  def verifyLogin(self):
    self.driver.execute_script("window.open('');")
    self.driver.switch_to.window(self.driver.window_handles[1])
    self.driver.get('https://www.primevideo.com')
    try:
      self.driver.find_element(By.CSS_SELECTOR, '[data-automation-id="nav-active-profile-name"]')
      return True
    except NoSuchElementException:
      self.login()
      return True

  def search(self, query):
    print('Searching Disney for:', query)