import os as Forge
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest



class GrabbingPayStubs(unittest.TestCase):

    chromeDriverLoc = "/Users/NewUser/Downloads/Automation/chromedriver"
    adpURL = 'https://online.adp.com/portal/login.html'
    userName = 'FBazile@Innotech1'
    passWord = 'red4red4'

    shit = 3
    ooosht = Forge.getcwd()
    print('this is the directory ', ooosht)
    downloadFilePath = '/Users/NewUser/Documents/Career'
    Forge.chdir(downloadFilePath)
    downloadPath = Forge.getcwd()
    print(downloadPath)

    def setUp(self):
        chromeOptions = webdriver.ChromeOptions()
        prefs = {'download.default_directory' : self.downloadFilePath}
        chromeOptions.add_experimental_option('prefs', prefs)
        self.cdriver = webdriver.Chrome(executable_path=self.chromeDriverLoc, chrome_options=chromeOptions)
        self.cdriver.get(self.adpURL)

    def test_Find_Login(self):
        login = self.cdriver.find_element_by_id('user_id')
        passField = self.cdriver.find_element_by_id('password')
        login.send_keys(self.userName + Keys.RETURN)
        passField.send_keys(self.passWord + Keys.RETURN)
        #time.sleep(30)
        self.assertTrue(True, 'huh')

    def tearDown(self):
        seix = 2
        print(seix)