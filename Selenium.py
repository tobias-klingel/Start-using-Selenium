from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException
from selenium.webdriver.common.keys import Keys


class UseSelenium():
    driver = None

#Setup
    def __init__(self):
        #self.driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
        self.driver = webdriver.Chrome(executable_path='/PycharmProjects/chromedriver')
        #self.driver = webdriver.PhantomJS(executable_path='/PycharmProjects/phantomjs')

    def __del__(self):
        self.driver.close()
        print "End"

#Navigate
    def callWebsite(self,url):
        self.driver.get(url)

    def goBack(self):
        self.driver.back()

#Controle
    def clickButton(self, type, cssType, cssSelector):
        try:
            sel = ("{}".format(type)+"["+ "{}".format(cssType)+"*='" + "{}".format(cssSelector)+"'")
            result = self.driver.find_element_by_css_selector(sel).click()
            return result
        except WebDriverException as errorWeb:
            print "Error in clickButton"
            print errorWeb

#Test object
    #Used to test if a object on a website is aviable
    def isCSS_selectorAvailable(self, type, cssSelector):
        try:
            result = self.driver.find_element_by_css_selector("{0}[{1}'".format(type, cssSelector))
            return result
        except WebDriverException as errorWeb:
            print "Error in isCSS_selectorAvailable: " + errorWeb
        except IndexError as errorIndex:
            print "Error in isCSS_selectorAvailable: " + errorIndex

#Get object