from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from dotenv import load_dotenv
import time
import os

class NetflixCrawler:
  def __init__(self, driver):
    self.driver = driver
    load_dotenv()

  def login(self):
    self.driver.get('https://www.netflix.com/login')
    time.sleep(5)

    email_input = self.driver.find_element(By.CSS_SELECTOR, '[data-uia="login-field"]')
    email = os.getenv('NETFLIX_EMAIL')
    time.sleep(5)
    email_input.send_keys(email)
    password_input = self.driver.find_element(By.CSS_SELECTOR, '[data-uia="password-field"]')
    password_input.send_keys(os.getenv('NETFLIX_PASSWORD'))
    login_button = self.driver.find_element(By.CSS_SELECTOR, '[data-uia="login-submit-button"]')
    login_button.click()
    time.sleep(5)
    profile = self.driver.find_element(By.CSS_SELECTOR, '[data-profile-guid="G3CN4XONGZHF3CJKMNUFR6NVDM"]')
    profile.click()

  def verifyLogin(self):
    self.driver.execute_script("window.open('');")
    self.driver.switch_to.window(self.driver.window_handles[3])
    self.driver.get('https://www.netflix.com/')
    try:
      self.driver.find_element(By.CSS_SELECTOR, '[data-profile-guid="G3CN4XONGZHF3CJKMNUFR6NVDM"]')
    except NoSuchElementException:
      self.login()
      return True

  def search(self, query):
    print('Searching Disney for:', query)