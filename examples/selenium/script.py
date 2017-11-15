# Import pyATS
from ats import aetest

# Import script libraries
from libs import page

# Selenium libraries
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class CommonSetup(aetest.CommonSetup):

    @aetest.subsection
    def connect_to_browser(self, testbed, browser):
        '''Connect to Google website via Firefox'''

        # Connect to browser with Remote
        driver = webdriver.Remote(
                      command_executor='http://172.25.192.112:4444/wd/hub',
                      desired_capabilities=DesiredCapabilities.FIREFOX)
        driver.get('http://google.com')

        # save to testscript parameters
        self.parent.parameters['driver'] = driver


class TestSearch(aetest.Testcase):
    '''Test case that opens search page and performs a search, expecting
    some sort of page result'''

    @aetest.setup
    def setup(self, driver, base_url):
        '''Make sure reached Google page'''
        self.main_page = page.GooglePage(driver)
        assert self.main_page.is_title_matches()

    @aetest.test
    def search(self, driver):
        '''Do a google search'''

        self.main_page.search_text_element = 'google awesome'
        self.main_page.click_search_button()

        search_result_page = page.SearchResultsPage(driver)
        title = self.main_page.search_text_element + ' - Google Search'
        assert search_result_page.is_title_matches(title)


class CommonCleanup(aetest.CommonCleanup):
    '''Disconnect from browser'''

    @aetest.subsection
    def disconnect_from_browser(self, driver):
        '''Disconnect from browser'''
        driver.close()
