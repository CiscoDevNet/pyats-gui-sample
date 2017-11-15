from .element import BasePageElement
from .locators import MainPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchTextElement(BasePageElement):
    """This class gets the search text from the specified locator"""

    #The locator for search box where search string is entered
    locator = 'q'

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class GooglePage(BasePage):

    #Declares a variable that will contain the retrieved text
    search_text_element = SearchTextElement()

    def is_title_matches(self):
        """Verifies that the hardcoded text "Google" appears in page title"""
        return "Google" in self.driver.title

    def click_search_button(self):
        """Triggers the search"""
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()

class SearchResultsPage(BasePage):
    """Search results page action methods come here"""

    def is_title_matches(self, title):
        """Verifies that the search appears in the title"""
        WebDriverWait(self.driver, 10).until(
                   EC.text_to_be_present_in_element((By.XPATH,
                                                    "/html/head/title"),
                                                    title))
        return True
