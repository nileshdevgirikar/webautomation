from resources import config
from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import Utilities.custom_logger as cl
import logging
import time
import os
from datetime import datetime, timedelta
from time import sleep


from selenium.webdriver.support.ui import Select

class SeleniumDriver():

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def wait_until_angular(self, TIMEOUT) -> None:
        java_script_to_load_angular = "var injector = window.angular.element('body').injector(); " \
                                      "var $http = injector.get('$http');" \
                                      "return ($http.pendingRequests.length === 0);"
        end_time = datetime.utcnow() + timedelta(seconds=TIMEOUT)
        print("wait for Angular Elements....")
        while datetime.utcnow() < end_time:
            try:
                if self.driver.execute_script(java_script_to_load_angular):
                    return
            except WebDriverException:
                continue
            sleep(1)
        raise TimeoutError("waiting for angular elements for too long")

    def screenShot(self, resultMessage):
        """
        Takes screenshot of the current open web page
        """
        fileName = resultMessage + "." + str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "../screenshots/"
        relativeFileName = screenshotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.log.info("Screenshot save to directory: " + destinationFile)
        except:
            self.log.error("### Exception Occurred when taking screenshot")


    def getTitle(self):
        return self.driver.title

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            self.log.info("Locator type " + locatorType +
                          " not correct/supported")
        return False

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element found with locator: " + locator +
                          " and  locatorType: " + locatorType)
        except:
            self.log.info("Element not found with locator: " + locator +
                          " and  locatorType: " + locatorType)
        return element

    def getElementList(self, locator, locatorType="id"):
        """
        NEW METHOD
        Get list of elements
        """
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_elements(byType, locator)
            self.log.info("Element list found with locator: " + locator +
                          " and locatorType: " + locatorType)
        except:
            self.log.info("Element list not found with locator: " + locator +
                          " and locatorType: " + locatorType)
        return element

    def elementClick(self, locator="", locatorType="id", element=None):
        """
        Click on an element -> MODIFIED
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                #self.waitForElement(locator)
                element = self.getElement(locator, locatorType)
            element.click()
            self.log.info("Clicked on element with locator: " + locator +
                          " locatorType: " + locatorType)
        except:
            self.log.info("Cannot click on the element with locator: " + locator +
                          " locatorType: " + locatorType)
            print_stack()

    def selectvaluefromDropdown(self, optionText, locator="", locatorType="id", element=None):
        """
        Click on an element -> MODIFIED
        Either provide element or a combination of locator and locatorType
        """
        try:
            element = Select(self.getElement(locator, locatorType))
            element.select_by_visible_text(optionText)
            self.log.info("Select value from element with locator: " + locator +
                          " locatorType: " + locatorType)
        except:
            self.log.info("Cannot select value from the element with locator: " + locator +
                          " locatorType: " + locatorType)

    def sendKeys(self, data, locator="", locatorType="id", element=None):
        """
        Send keys to an element -> MODIFIED
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            element.clear()
            element.send_keys(data)
            self.log.info("Sent data on element with locator: " + locator +
                          " locatorType: " + locatorType)
        except:
            self.log.info("Cannot send data on the element with locator: " + locator +
                  " locatorType: " + locatorType)
            print_stack()

    def sendKeysAndEnter(self, data, locator="", locatorType="id", element=None):
        """
        Send keys to an element -> MODIFIED
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement( locator, locatorType )
            element.clear()
            element.send_keys( data )
            element.send_keys( Keys.ENTER )
            self.log.info( "Sent data on element with locator: " + locator +
                           " locatorType: " + locatorType )
        except:
            self.log.info( "Cannot send data on the element with locator: " + locator +
                           " locatorType: " + locatorType )
            print_stack()

    def clearField(self, locator="", locatorType="id"):
        """
        Clear an element field
        """
        element = self.getElement(locator, locatorType)
        element.clear()
        self.log.info("Clear field with locator: " + locator +
                      " locatorType: " + locatorType)

    def getText(self, locator="", locatorType="id", element=None, info=""):
        """
        NEW METHOD
        Get 'Text' on an element
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator: # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            text = element.text
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                self.log.info("Getting text on element :: " +  info)
                self.log.info("The text is :: '" + text + "'")
                text = text.strip()
        except:
            self.log.error("Failed to get text on element " + info)
            text = None
        return text

    def isElementPresent(self, locator="", locatorType="id", element=None):
        """
        Check if element is present -> MODIFIED
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info("Element present with locator: " + locator +
                              " locatorType: " + locatorType)
                return True
            else:
                self.log.info("Element not present with locator: " + locator +
                              " locatorType: " + locatorType)
                return False
        except:
            print("Element not found")
            return False

    def isElementDisplayed(self, locator="", locatorType="id", element=None):
        """
        NEW METHOD
        Check if element is displayed
        Either provide element or a combination of locator and locatorType
        """
        isDisplayed = False
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            if element is not None:
                isDisplayed = element.is_displayed()
                self.log.info("Element is displayed" )
            else:
                self.log.info("Element not displayed")
            return isDisplayed
        except:
            self.log.info("Element not found")
            return False

    def elementPresenceCheck(self, locator, byType):
        """
        Check if element is present
        """
        try:
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0:
                self.log.info("Element present with locator: " + locator +
                              " locatorType: " + str(byType))
                return True
            else:
                self.log.info("Element not present with locator: " + locator +
                              " locatorType: " + str(byType))
                return False
        except:
            self.log.info("Element not found")
            return False

    def waitForElement(self, locator, locatorType="id",
                       timeout=2, pollFrequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                  " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout=timeout,
                                 poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType, locator)))
            self.log.info("Element appeared on the web page")
        except:
            self.log.info("Element not appeared on the web page")
        return element

    def waitForElementInVisible(self, locator, locatorType="id",
                                timeout=5, pollFrequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                          " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout=timeout,
                                 poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.invisibility_of_element((byType, locator)))
            self.log.info("Element is visible appeared on the web page")
        except:
            self.log.info("Element not appeared on the web page")
        return element

    NG_WRAPPER = '%(prefix)s' \
                 'angular.element(document.querySelector(\'[data-ng-app]\')|(document).' \
                 'injector().get(\'$browser\').notifyWhenNoOutStandingRequests(%(handler)s)' \
                 '%(suffix)s'

    # def wait_until_angular_ready(self, timeout=None, error=None):
    #     """Waits until [https://goo.gl/Kzz8Y3|AngularJS] is ready to process the next request or
    #     ``timeout`` expires.
    #
    #     Arguments:
    #     - ``timeout``: The maximum value to wait for [https://goo.gl/Kzz8Y3|AngularJS]
    #                    to be ready to process the next request.
    #                    See `introduction` for more information about ``timeout`` and
    #                    its default value.
    #     - ``error``: The value that would be use to override the default error message.
    #
    #     Examples:
    #     | Wait Until Angular Ready | 15s |
    #     """
    #     # pylint: disable=no-member
    #     timeout = self._get_timeout_value(timeout, self._implicit_wait_in_secs)
    #     if not error:
    #         error = 'AngularJS is not ready in %s' % self._format_timeout(timeout)
    #     # we add more validation here to support transition
    #     # between AngularJs to non AngularJS page.
    #     # pylint: disable=no-member
    #     script = self.NG_WRAPPER % {'prefix': 'var cb=arguments[arguments.length-1];'
    #                                           'if(window.angular){',
    #                                 'handler': 'function(){cb(true)}',
    #                                 'suffix': '}else{cb(true)}'}
    #     # pylint: disable=no-member
    #     browser = self._current_browser()
    #     browser.set_script_timeout(timeout)
    #     # pylint: disable=bare-except
    #     try:
    #         WebDriverWait(browser, timeout, self._inputs['poll_frequency']). \
    #             until(lambda driver: driver.execute_async_script(script), error)
    #     except TimeoutException:
    #         # prevent double wait
    #         pass
    #     except:
    #         self._debug(exc_info()[0])
    #         # still inflight, second chance. let the browser take a deep breath...
    #         time.sleep(self._inputs['browser_breath_delay'])
    #         try:
    #             WebDriverWait(browser, timeout, self._inputs['poll_frequency']). \
    #                 until(lambda driver: driver.execute_async_script(script), error)
    #         except:
    #             # instead of halting the process because AngularJS is not ready
    #             # in <TIMEOUT>, we try our luck...
    #             self._debug(exc_info()[0])
    #         finally:
    #             browser.set_script_timeout(self._timeout_in_secs)
    #     finally:
    #         browser.set_script_timeout(self._timeout_in_secs)

    def webScroll(self, direction="up"):
        """
        NEW METHOD
        """
        if direction == "up":
            # Scroll Up
            self.driver.execute_script("window.scrollBy(0, -1000);")

        if direction == "down":
            # Scroll Down
            self.driver.execute_script("window.scrollBy(0, 200);")

    def elementScroll(self, tablescroll, elementlocator):
        """
        NEW METHOD
        """
        dragger = ActionChains(self.driver)
        self.draggablePartOfScrollbar = self.driver.find_element_by_xpath(tablescroll)
        numberOfPixelsToDragTheScrollbarDown = 25
        findFlag = False
        while not findFlag:
            dragger.move_to_element(self.draggablePartOfScrollbar). \
                click_and_hold().move_by_offset(0, numberOfPixelsToDragTheScrollbarDown).release().perform()
            findFlag = self.isElementDisplayed(elementlocator, locatorType="xpath")
            if findFlag:
                break
        return findFlag

    def executeJavaScript(self, locator, locatorType="id", element=None):
        """
        Click on an element -> MODIFIED
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                self.element = self.driver.find_element_by_xpath(locator)
                self.driver.execute_script("arguments[0].click()", self.element)
            self.log.info( "Clicked on element with locator: " + locator +
                           " locatorType: " + locatorType)
        except:
            self.log.info("Cannot click on the element with locator: " + locator +
                          " locatorType: " + locatorType)
            print_stack()

    def iselementSelected(self, locator, locatorType=""):
        """
        Check if element is present
        """
        try:
            element = self.driver.find_element_by_xpath(locator)
            flag = element.is_selected()
            if flag == True:
                self.log.info("Element is selected with locator: " + locator +
                              " locatorType: ")
                return True
            else:
                self.log.info("Element not selected with locator: " + locator +
                              " locatorType: ")
                return False
        except:
            self.log.info("Element not found")
            return False

    def wait_for_page_load(self, timeout=10):
        time.sleep( timeout )

    def wait_and_refresh(self, timeout=10):
        time.sleep(timeout)
        self.driver.refresh()

    WAIT_FOR_SCRIPT = """
            callback = arguments[arguments.length - 1];
            try {
                var testabilities = window.getAllAngularTestabilities();
                var count = testabilities.length;
                var decrement = function() {
                count--;
                if (count === 0) {
                  callback('completed');
                    }
                };
                testabilities.forEach(function(testability) {
                    testability.whenStable(decrement);
                });
             } catch (err) {
                callback(err.message);
             }
            """

    def wait_for_angular(self, timeout):
        self.driver.set_script_timeout(timeout)
        self.driver.execute_async_script(self.WAIT_FOR_SCRIPT)
