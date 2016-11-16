import os as Forge
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import unittest
import shutil


class GrabbingPayStubs(unittest.TestCase):

    chromeDriverLoc = "/Users/NewUser/Downloads/Automation/chromedriver"
    adpURL = 'https://online.adp.com/portal/login.html'
    userName = 'FBazile@Innotech1'
    passWord = ''

    downloadFilePath = '/Users/NewUser/Documents/Career/2'
    Forge.chdir(downloadFilePath)
    folderNames = []

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
        self.cdriver.find_element_by_partial_link_text('Pay Statement').click()

        #I Know Kung Fu..
        moko = int(self.cdriver.find_element_by_xpath('//*[contains (@id, "viewns_Z7")]/b').text)
        self.cdriver.execute_script("$(window.open('https://twitter.com'))")
        self.cdriver.switch_to_window(self.cdriver.window_handles[-1])
        #time.sleep(12)
        self.cdriver.find_element_by_xpath('//*[@id="doc"]/div[1]/div/div[2]/div/a[2]/span').click()
        time.sleep(30)
        self.cdriver.close()
        time.sleep(900)
        #whenToStop = True
        count = 0
        while True:

            #Grab 1st column names & years for paystubs
            whiskey2 = []

            whiskey = self.cdriver.find_elements_by_partial_link_text('201')
            for webElement in whiskey:
                whiskey2.append(webElement.text)

                yearCapture = webElement.text[6:]
                if yearCapture not in self.folderNames: self.folderNames.append(yearCapture)

            #iterating thru list of pay statements and grabbing pdfs
            for lnk in whiskey2:

                #pdf name capture & click on link
                pdf = lnk.replace('/', '.')
                pdfName = (pdf + '.pdf')
                self.cdriver.find_element_by_link_text(lnk).click()

                tango = self.cdriver.find_element_by_id('embedPdf').get_attribute('src')
                self.cdriver.get(tango)
                time.sleep(4)
                Forge.rename('download.pdf', pdfName)
                count += 1

                self.cdriver.find_element_by_id('cancelTopCenter').click()

            try:
                self.cdriver.find_element_by_xpath('//*[@title="Click to display the next page of results"]').click()
                time.sleep(6)
            except NoSuchElementException: break
                #whenToStop = False

        self.assertEqual(moko, count, "Number of Downloads does not match Number of entries")

    def tearDown(self):
        for year in self.folderNames:
            Forge.mkdir(year)

            txtF = year + '.pdf'
            yrFolder = self.downloadFilePath + '/' + year
            pdfs_In_Folder = Forge.listdir(self.downloadFilePath)

            for pdf in pdfs_In_Folder:
                if txtF in pdf:
                    shutil.move(pdf, yrFolder)