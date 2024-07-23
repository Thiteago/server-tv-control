from selenium import webdriver
from .crawlers.disney_crawler import DisneyCrawler
from .crawlers.prime_crawler import PrimeCrawler
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


class SearchController:
  def __init__(self):
    self.chrome_driver_path = 'C:\\dependencies_dev\\chromedriver-win64\\chromedriver.exe'
    self.service = Service(executable_path=self.chrome_driver_path)
    self.options = Options()
    self.options.add_argument('--headless')
    self.driver = webdriver.Chrome(service=self.service, options=self.options)

    self.crawlers = [
      DisneyCrawler(driver=self.driver),
      PrimeCrawler(driver=self.driver)
    ]

    self.__verify_logins()

  def search(self, search_query, platform):
    for crawler in self.crawlers:
      if platform == 'disney':
        crawler.search(search_query)
    return True

  def __verify_logins(self):
    for crawler in self.crawlers:
      crawler.verifyLogin()
      
