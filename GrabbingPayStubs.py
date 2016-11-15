import os as Forge
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import unittest



class GrabbingPayStubs(unittest.TestCase):

    chromeDriverLoc = "/Users/NewUser/Downloads/Automation/chromedriver"
    adpURL = 'https://online.adp.com/portal/login.html'
    userName = 'FBazile@Innotech1'
    passWord = 'red4red4'

    ooosht = Forge.getcwd()
    print('this is the directory ', ooosht)

    downloadFilePath = '/Users/NewUser/Documents/Career/2'
    Forge.chdir(downloadFilePath)

    downloadPath = Forge.getcwd()
    print(downloadPath)

    def setUp(self):
        chromeOptions = webdriver.ChromeOptions()
        prefs = {'plugins.plugins_list': [{'enabled':False, 'name': 'Chrome PDF Viewer'}],
                 'download.default_directory' : self.downloadFilePath}
        chromeOptions.add_experimental_option('prefs', prefs)
        self.cdriver = webdriver.Chrome(executable_path=self.chromeDriverLoc, chrome_options=chromeOptions)
        self.cdriver.get(self.adpURL)


    def test_Find_Login(self):
        login = self.cdriver.find_element_by_id('user_id')
        passField = self.cdriver.find_element_by_id('password')
        login.send_keys(self.userName)
        passField.send_keys(self.passWord + Keys.RETURN)

        self.cdriver.find_element_by_id('menuHit.node2').click()

        #time.sleep(2)
        self.cdriver.find_element_by_partial_link_text('Pay Statement').click()

        time.sleep(4)
        #foxtrot = self.cdriver.find_element_by_xpath('//*[@title="Click to display the next page of results"]')

        whenToStop = True
        while whenToStop:

            #Grab 1st column names
            whiskey2 = []
            whiskey = self.cdriver.find_elements_by_partial_link_text('201')
            for webElement in whiskey:
                whiskey2.append(webElement.text)

            #iterating thru list of pay statements and grabbing pdfs
            for lnk in whiskey2:

                #pdf name capture & click on link
                pdf = lnk.replace('/', '.')
                pdfName = (pdf + '.pdf')
                self.cdriver.find_element_by_link_text(lnk).click()

                time.sleep(4)

                tango = self.cdriver.find_element_by_id('embedPdf').get_attribute('src')
                self.cdriver.get(tango)
                time.sleep(4)
                Forge.rename('download.pdf', pdfName)
                time.sleep(4)

                self.cdriver.find_element_by_id('cancelTopCenter').click()
                time.sleep(6)

            #clicking to next page of results & refreshing element of page
            foxtrot = self.cdriver.find_element_by_xpath('//*[@title="Click to display the next page of results"]')
            if foxtrot.is_displayed():
                foxtrot.click()
                time.sleep(6)
            else: whenToStop = False
            #newBlade = self.cdriver.find_element_by_xpath('//*[@title="Click to display the next page of results"]').is_displayed()
                #if not newBlade:

        #time.sleep(10)

        self.assertTrue(True, 'huh')

    def tearDown(self):
        print(self.downloadPath)