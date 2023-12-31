import selenium.common
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

CHROME_OPTIONS = webdriver.ChromeOptions()
CHROME_OPTIONS.add_experimental_option("detach",True)

SEARCH = 'ZX25R'

class YoutubeWatcher:
    def __init__(self):
        self.driver = webdriver.Chrome(CHROME_OPTIONS)
        self.driver.maximize_window()

    def open_site(self):
        self.driver.get('https://www.youtube.com/')
        time.sleep(3)

    def locate_and_search(self):
        self.search_bar = self.driver.find_element(By.NAME,'search_query')
        time.sleep(2)
        self.search_bar.send_keys(SEARCH)
        time.sleep(2)

        self.search_button = self.driver.find_element(By.ID,'search-icon-legacy')
        time.sleep(2)
        self.search_button.click()

        time.sleep(3)
        #Via Full XPATH
        self.click_video = self.driver.find_element(By.XPATH,'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]')
        time.sleep(2)
        self.click_video.click()

bot = YoutubeWatcher()
time.sleep(1)
bot.open_site()
time.sleep(1)
bot.locate_and_search()
