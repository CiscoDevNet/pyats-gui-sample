'''job.py

This is an easypy job example intended to run WebDriver testscript.

Webdriving package contains a collection of tools and base classes intended to
simplify and standardize how automation engineers develop Selenium based
libraries.

Arguments:
    This job requires one argument (testbed) to be passed 
    testbed: the path to testbed yaml file

Examples:
    # TO run under easypy
    bash$ easypy job.py -testbed_file ../etc/testbed.yaml

References:
   For the complete and up-to-date user guide on pyATS, visit:
    https://developer.cisco.com/site/pyats/docs/
'''


__author__ = 'Jean-Benoit Aubin <jeaubin@cisco.com>'
__copyright__ = 'Copyright 2017, Cisco Systems'
__email__ = 'pyats-support-ext@cisco.com'
__date__= 'Nov 16, 2017'

import os

from ats.easypy import run

SCRIPT_DIR = os.path.dirname(os.path.dirname(__file__))


def main():

    run(testscript = os.path.join(SCRIPT_DIR, 'script.py'),
        browser = 'firefox',
        base_url = 'http://www.google.com/')
