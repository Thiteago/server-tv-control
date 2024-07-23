from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import os

class DisneyCrawler:
  def __init__(self, driver):
    self.driver = driver

  def login(self):
    self.driver.get('https://www.disneyplus.com/en-br')
    login_button = self.driver.find_element(By.CSS_SELECTOR, '[data-gv2-name="log_in"]')
    login_button.click()
    time.sleep(5)
    email_input = self.driver.find_element(By.CSS_SELECTOR, 'input[id="email"]')
    email_input.send_keys(os.getenv('DISNEY_PLUS_EMAIL'))
    continue_button = self.driver.find_element(By.CSS_SELECTOR, '[data-testid="continue-btn"]')
    continue_button.click()
    time.sleep(5)
    password_input = self.driver.find_element(By.CSS_SELECTOR, 'input[id="password"]')
    password_input.send_keys(os.getenv('DISNEY_PLUS_PASSWORD'))
    login_button = self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    login_button.click()
    time.sleep(5)
    profiles = self.driver.find_elements(By.CSS_SELECTOR, '[data-testid="selected-avatar-image"]')
    first_profile = profiles[0]
    first_profile.click()

  def verifyLogin(self):
    self.driver.get('https://www.disneyplus.com/home')
    try:
      self.driver.find_element(By.CSS_SELECTOR, '[data-gv2-name="log_in"]')
      return True
    except NoSuchElementException:
      self.login()
      return True

  def search(self, query):
    print('Searching Disney for:', query)