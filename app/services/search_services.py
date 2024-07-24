import threading
from selenium import webdriver
from .crawlers.disney_crawler import DisneyCrawler
from .crawlers.prime_crawler import PrimeCrawler
from .crawlers.max_crawler import MaxCrawler
from .crawlers.netflix_crawler import NetflixCrawler
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
      PrimeCrawler(driver=self.driver),
      MaxCrawler(driver=self.driver),
      NetflixCrawler(driver=self.driver)
    ]

    self.__verify_logins()

  def search(self, search_query, platform):
    results = {
      'disney': [],
      'prime': [],
      'max': [],
      'netflix': []
    }

    events = []
    threads = []
    
    for crawler in self.crawlers:
      if platform == 'disney':
        event = threading.Event()
        events.append(event)
        thread = threading.Thread(target=self._search_in_crawler, args=(crawler, search_query, results, platform, event))
        threads.append(thread)
        thread.start()

    for event in events:
      event.wait()

    return results

  def __verify_logins(self):
    for crawler in self.crawlers:
      crawler.verifyLogin()

  def _search_in_crawler(self, crawler, search_query, results, platform, event):
    results[platform] = crawler.search(search_query)
    event.set()
      
