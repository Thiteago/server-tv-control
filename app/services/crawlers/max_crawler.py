from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from pyshadow.main import Shadow
from dotenv import load_dotenv
import time
import os

class MaxCrawler:
  def __init__(self, driver):
    self.driver = driver
    load_dotenv()

  def login(self):
    self.driver.get('https://auth.max.com/login')
    time.sleep(5)

    cookie_button = self.driver.find_element(By.CSS_SELECTOR, 'button[id="onetrust-accept-btn-handler"]')
    cookie_button.click()
    time.sleep(5)

    shadow = Shadow(self.driver)

    shadow_parent = shadow.find_element('gi-login-username-and-mvpd')
    email_input = shadow.find_element(shadow_parent, '[data-testid="gisdk.gi-login-username.email_field"]')
    email = os.getenv('MAX_EMAIL')
    time.sleep(5)
    email_input.send_keys(email)
    password_input = shadow.find_element(shadow_parent, 'input[id="login-password-input"]')
    password_input.send_keys(os.getenv('MAX_PASSWORD'))
    login_button = shadow.find_element(shadow_parent, '[data-testid="gisdk.gi-login-username.signIn_button"]')
    login_button.click()
    time.sleep(5)
    profiles_list = self.driver.find_elements(By.CSS_SELECTOR, '[data-test-profile-id="0bda1dbe-e019-4e6c-8616-1d74d5f602a0"]')
    profile = profiles_list[0].find_element(By.CSS_SELECTOR, '[data-testid="edit_avatar_selection_button"]')
    profile.click()

  def verifyLogin(self):
    self.driver.execute_script("window.open('');")
    self.driver.switch_to.window(self.driver.window_handles[2])
    self.driver.get('https://play.max.com/')
    try:
      self.driver.find_element(By.CSS_SELECTOR, '[data-testid="profile_button"]')
    except NoSuchElementException:
      self.login()
      return True

  def search(self, query):
    print('Searching Disney for:', query)