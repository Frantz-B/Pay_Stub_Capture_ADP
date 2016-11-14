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
    #pysb = '#menuHit\2e node2'
    #shit = 3

    ooosht = Forge.getcwd()
    print('this is the directory ', ooosht)

    downloadFilePath = '/Users/NewUser/Documents/Career'
    Forge.chdir(downloadFilePath)

    downloadPath = Forge.getcwd()
    print(downloadPath)

    def setUp(self):
        chromeOptions = webdriver.ChromeOptions()
        prefs = {'plugins.plugins_list': [{'enabled':False, 'name': 'Chrome PDF Viewer'}], 'download.default_directory' : self.downloadFilePath}
        chromeOptions.add_experimental_option('prefs', prefs)
        self.cdriver = webdriver.Chrome(executable_path=self.chromeDriverLoc, chrome_options=chromeOptions)
        self.cdriver.get(self.adpURL)


    def test_Find_Login(self):
        login = self.cdriver.find_element_by_id('user_id')
        passField = self.cdriver.find_element_by_id('password')
        login.send_keys(self.userName)
        passField.send_keys(self.passWord + Keys.RETURN)

        #time.sleep(4)
        self.cdriver.find_element_by_id('menuHit.node2').click()

        time.sleep(2)
        #self.cdriver.find_element_by_link_text('Pay Sta')
        self.cdriver.find_element_by_partial_link_text('Pay Statement').click()

        #self.cdriver.find_element_by_css_selector('#dropMenu>table>tbody>tr:nth-child(2)>td>nobr>a').click()
        #select.select_by_visible_text('Pay Statment')
        # time.sleep(10)
        #self.cdriver.find_element_by_partial_link_text('2016').click()
        time.sleep(4)
        foxtrot = self.cdriver.find_element_by_xpath('//*[@title="Click to display the next page of results"]')
        while foxtrot.is_displayed():
            whiskey2 = []
            whiskey = self.cdriver.find_elements_by_partial_link_text('201')
            for webElement in whiskey:
                whiskey2.append(webElement.text)

        #main_chrome = self.cdriver.current_window_handle

            for lnks in whiskey2:

                pdf = lnks.replace('/', '.')
                pdfName = (pdf + '.pdf')
                self.cdriver.find_element_by_link_text(lnks).click()

            #lnks.send_keys(Keys.COMMAND + Keys.ENTER)
            #self.cdriver.execute_script("window.open('www.google.com');", '_blank')
            #self.cdriver.execute_script('''window.open("about:blank", "_blank");''')
                time.sleep(2)
            #self.cdriver.get(lnks.get_attribute('href'))
            #lnks.send_keys(Keys.CONTROL + Keys.TAB)
            #self.cdriver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + Keys.NUMPAD2)
            #time.sleep(16)

                tango = self.cdriver.find_element_by_id('embedPdf').get_attribute('src')
                self.cdriver.get(tango)
                time.sleep(4)
                Forge.rename('download.pdf', pdfName)
                time.sleep(4)

            #self.cdriver.close()
            #time.sleep(6)
            #self.cdriver.refresh()
                self.cdriver.find_element_by_id('cancelTopCenter').click()
                time.sleep(6)
            foxtrot = self.cdriver.find_element_by_xpath('//*[@title="Click to display the next page of results"]')
            foxtrot.click()
            time.sleep(4)
            foxtrot = self.cdriver.find_element_by_xpath('//*[@title="Click to display the next page of results"]')
        #self.cdriver.find_element_by_css_selector('#icon').click()
        time.sleep(10)
        #tango = self.cdriver.find_element_by_id('embedPdf').get_attribute('src')
        #self.cdriver.get(tango)

        self.assertTrue(True, 'huh')

    def tearDown(self):
        #Forge.rename('download.pdf', 'nuts.pdf')
        print(self.downloadPath)