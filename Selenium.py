from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException
from selenium.webdriver.common.keys import Keys
import time


class UseSelenium():
    driver = None

#Setup
    def __init__(self):
        #self.driver = webdriver.Firefox(executable_path='/usr/geckodriver')
        self.driver = webdriver.Chrome(executable_path='/Projects/chromedriver')
        #self.driver = webdriver.PhantomJS(executable_path='/Projects/phantomjs')

        ##Run one of these functions instead the command above to use Selenium with a proxy
        #webProxyFirefox()
        #webProxyChrome()

    #Proxy configuration for Firefox browser
    def webProxyFirefox(self):
        profile = webdriver.FirefoxProfile()
        profile.set_preference("network.proxy.type", 1)
        profile.set_preference("network.proxy.http", 'xxx.xxx.xxx.xxx')
        profile.set_preference("network.proxy.http_port", 8080)
        profile.set_preference("network.proxy.ssl", 'xxx.xxx.xxx.xxx')
        profile.set_preference("network.proxy.ssl_port", 8080)
        self.driver = webdriver.Firefox(firefox_profile=profile,
                                        executable_path='/Projects/chromedriver')

    #Proxy configuration for Chrome browser
    def webProxyChrome(self):
        self.proxyChrome = "xxx.xxx.xxx.xxx:8080"
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--proxy-server=%s' % self.proxyChrome)
        self.driver = webdriver.Chrome(chrome_options=chrome_options,
                                       executable_path='/Projects/chromedriver')
        # chrome.get("http://whatismyipaddress.com")

    #Close webbrowser instance after program finished
    def __del__(self):
        self.driver.close()
        print "End"

###################################################################################
#Navigate

    #Open a website by URL
    def callWebsite(self,url):
        self.driver.get(url)

    #Return to prevoiuse page
    def goBack(self):
        self.driver.back()

    #Scroll on main page
    def scrollPage(self):
        try:
            body = self.driver.find_element_by_css_selector('body')
            body.send_keys(Keys.END)
        except WebDriverException as errorWeb:
            print errorWeb

###################################################################################
#Controle

    #Click a button on page (type, cssType, cssSelector)
    def clickButton(self, type, cssType, cssSelector):
        try:
            sel = ("{}".format(type)+"["+ "{}".format(cssType)+"*='" + "{}".format(cssSelector)+"'")
            result = self.driver.find_element_by_css_selector(sel).click()
            return result
        except WebDriverException as errorWeb:
            print "Error in clickButton"
            print errorWeb

    #Log in ith credentials (user, password)
    def logIn(self, user, password):
        time.sleep(2)
        driver.find_element_by_name("username").send_keys(user)
        driver.find_element_by_name("password").send_keys(password)
        driver.find_element_by_name("password").send_keys(Keys.RETURN)

###################################################################################
#Test object

    #Used to test if an object is on a website available (type, cssSelector - Return none or object)
    def isCSS_selectorAvailable(self, type, cssSelector):
        try:
            result = self.driver.find_element_by_css_selector("{0}[{1}'".format(type, cssSelector))
            return result
        except WebDriverException as errorWeb:
            print "Error in isCSS_selectorAvailable: " + errorWeb
        except IndexError as errorIndex:
            print "Error in isCSS_selectorAvailable: " + errorIndex

    #Get the url of current page (Return url)
    def getCurrentUrl(self):
        try:
            currentUrl = self.driver.current_url
            currentUrl = unicodedata.normalize('NFKD', currentUrl).encode('ascii', 'ignore')
            return currentUrl
        except WebDriverException as errorWeb:
            print errorWeb
            return False

###################################################################################

#Get object