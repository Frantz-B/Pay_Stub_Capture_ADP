import os as Forge
from selenium import webdriver
import time
import unittest



class GrabbingPayStubs(unittest.TestCase):

    chromeDriverLoc = "/Users/NewUser/Downloads/Automation/chromedriver"
    adpURL = 'https://online.adp.com/portal/login.html'

    shit = 3
    ooosht = Forge.getcwd()
    print('this is the directory ', ooosht)
    downloadFilePath = '/Users/NewUser/Documents/Career'
    Forge.chdir(downloadFilePath)
    downloadPath = Forge.getcwd()
    print(downloadPath)

    def setUp(self):
        chromeOptions = webdriver.ChromeOptions()
        prefs = {'download.default_directory' : downloadFilePath}
        chromeOptions.add_experimental_option('prefs', prefs)
        self.cdriver = webdriver.Chrome(executable_path=chromeDriverLoc, chrome_options=chromeOptions)
        self.cdriver.get(adpURL)