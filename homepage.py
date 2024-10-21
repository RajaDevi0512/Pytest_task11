from selenium import webdriver
from selenium.webdriver.common.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

class SauceDemo_Automation:
    # Init Constructor, Passing url
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome()

    # starting automation method 
    def start_automation(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        sleep(5)
        return True
    
    # shutdown method
    def shutdown(self):
        # quit() method close all the browser instances
        self.driver.quit()
        sleep(5)

    # fetch the title
    def fetch_title(self):
        if self.start_automation():
            return self.driver.title
        else:
            return False
        
    # fetch the URL
    def fetch_url(self):
        if self.start_automation():
            return self.driver.current_url
        else:
            return False

    # fetch the webpage content
    def fetch_webpage_content(self):
        page_content = self.driver.page_source
        with open('Webpage_task11.txt', 'a') as file:
            file.write(page_content)
