from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

URL_login, URL_main = 'https://hcs.eduro.go.kr/#/relogin', 'https://hcs.eduro.go.kr/#/main'

class s :
    def setdata(self,datalist):
        self.password = str(datalist[-1])
        self.school = list([datalist[1],datalist[2],datalist[3]])
        self.name = str(datalist[0])
        self.day = str(datalist[4])
            
    def schoolsearch(self):
        time.sleep(1)
        # driver.implicitly_wait(0.5)
        search = driver.find_element_by_css_selector('#WriteInfoForm > table > tbody > tr:nth-child(1) > td > button')
        search.send_keys(Keys.ENTER)
        search = driver.find_element_by_css_selector('#sidolabel')
        select = Select(search)
        select.select_by_visible_text(self.school[0])
        search = driver.find_element_by_css_selector('#crseScCode')
        select = Select(search)
        select.select_by_visible_text(self.school[1])
        search = driver.find_element_by_css_selector('#orgname')
        search.send_keys(str(self.school[2]))
        search = driver.find_element_by_css_selector('#softBoardListLayer > div.layerContentsWrap > div.layerSchoolSelectWrap > table > tbody > tr:nth-child(3) > td:nth-child(3) > button')
        search.send_keys(Keys.ENTER)
        search = driver.find_element_by_css_selector('#softBoardListLayer > div.layerContentsWrap > div.layerSchoolSelectWrap > ul > li > a')
        search.send_keys(Keys.ENTER)
        search = driver.find_element_by_css_selector('#softBoardListLayer > div.layerContentsWrap > div.layerBtnWrap > input')
        search.send_keys(Keys.ENTER)

    def check(self) :
        time.sleep(1)
        # driver.implicitly_wait(0.5)
        search = driver.find_element_by_css_selector('#user_name_input')
        search.send_keys(str(self.name))
        search = driver.find_element_by_css_selector('#birthday_input')
        search.send_keys(str(self.day))
        search = driver.find_element_by_css_selector('#btnConfirm')
        search.send_keys(Keys.ENTER)

    def num(self) :
        # driver.implicitly_wait(5)
        time.sleep(1)
        search = driver.find_element_by_css_selector('#WriteInfoForm > table > tbody > tr > td > input')
        search.send_keys(str(self.password))
        search = driver.find_element_by_css_selector('#btnConfirm')
        search.send_keys(Keys.ENTER)

    def selfcheck() :
        # driver.implicitly_wait(5)
        time.sleep(2)
        search = driver.find_element_by_css_selector('#container > div > section.memberWrap > div:nth-child(2) > ul > li > a') ##container > div > section.memberWrap > div:nth-child(2) > ul > li > a
        search.send_keys(Keys.ENTER)
        search = driver.find_element_by_css_selector('#survey_q1a1')
        search.click()
        search = driver.find_element_by_css_selector('#survey_q2a1')
        search.click()
        search = driver.find_element_by_css_selector('#survey_q3a1')
        search.click()   
        search = driver.find_element_by_css_selector('#btnConfirm')
        search.click()

    
def main() :
    global driver
    start = s
    driver = webdriver.Chrome(executable_path='C:/Users/inwoo/Google Drive/myFile_inwoo/hobby/파이썬/python/chromedriver.exe')
    driver.implicitly_wait(1)
    driver.get(URL_login)
    search = driver.find_element_by_css_selector('#btnConfirm2')
    search.send_keys(Keys.ENTER)
    driver.implicitly_wait(3)
    s.schoolsearch(start)
    s.check(start)
    s.num(start)
    s.selfcheck()

    # search = driver.find_element_by_class_name("input_text_common")
    # try:
    #     search = driver.find_element_by_css_selector('#secondaryPwForm > table > tbody > tr > td > input')
    #     search.send_keys(str(password))
    # except :
    time.sleep(1)

    print('end')