from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException
from selenium.webdriver.common.keys import Keys


class UseSelenium():
    driver = None

    def __init__(self):
        #self.driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
        self.driver = webdriver.Chrome(executable_path='/Users/PycharmProjects/chromedriver') #12/2018
        #self.driver = webdriver.PhantomJS(executable_path='/Users/tokl/PycharmProjects/instagram_follower/phantomjs')

    def __del__(self):
        self.driver.close()
        print "End"

    def callWebsite(self,url):
        self.driver.get(url)
