#!/bin/env python

'''script.py

This is a testscript example intended to walk users through WebDriver
testing with pyATS.

Webdriving package contains a collection of tools and base classes intended to
simplify and standardize how automation engineers develop Selenium based
libraries.

Arguments:
    This script requires one script argument (testbed) to be passed in when run
    under standalone execution for demonstration purposes.
    testbed: the path to testbed yaml file

Examples:
    # to run under standalone execution
    bash$ python script.py -testbed_file etc/testbed.yaml

References:
    For the complete and up-to-date user guide on pyATS, visit:
    https://developer.cisco.com/site/pyats/docs/
'''

__author__ = 'Jean-Benoit Aubin <jeaubin@cisco.com>'
__copyright__ = 'Copyright 2017, Cisco Systems'
__email__ = 'pyats-support-ext@cisco.com'
__date__= 'Nov 16, 2017'


# Import pyATS
from ats import aetest

# Import script libraries
from libs import google

class CommonSetup(aetest.CommonSetup):
    '''Setup for the testscript'''

    @aetest.subsection
    def connect_to_browser(self, testbed, browser = 'firefox'):
        '''Connect to Google website via browser'''
        
        # get device
        driver = testbed.devices[browser]

        # connect via webdriver
        driver.connect(via = 'webdriver')

        # save to paramters
        self.parent.parameters['driver'] = driver


class TestSearch(aetest.Testcase):
    '''Test case that opens search page and performs a search, expecting
    some sort of page result'''

    @aetest.setup
    def setup(self, driver, base_url = 'http://www.google.com/'):

        # create page object instance
        self.page = google.GoogleSearch(driver = driver, timeout = 10,
                                        base_url = base_url)

        # open the page
        self.page.open()

    @aetest.test
    def test_search(self):

        # Search for google is awesome
        # Automatically click on the button
        self.page.search('google is awesome')

        # Wait for the page to load
        self.page.wait.until.title_contains('Google Search')


class CommonCleanup(aetest.CommonCleanup):

    @aetest.subsection
    def disconnect_from_browser(self, driver):
        
        # Disconnect from the browser 
        driver.destroy()


if __name__ == '__main__':

    # local imports
    import argparse
    from ats.topology import loader

    parser = argparse.ArgumentParser(description = "standalone parser")
    parser.add_argument('--testbed', dest = 'testbed',
                        type = loader.load)

    # parse args
    args, unknown = parser.parse_known_args()

    # and pass all arguments to aetest.main() as kwargs
    aetest.main(**vars(args)) 
