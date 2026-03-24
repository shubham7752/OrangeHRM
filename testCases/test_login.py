import pytest
import time
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL=ReadConfig.getApplicationURl()
    username=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()

    logger=LogGen.loggen()


    def test_homePageTitle(self,setup):

        self.logger.info("***************Test_001_Login***************")
        self.logger.info("*************** Verifying Home Page Title ***************")
        self.driver=setup
        self.driver.get(self.baseURL)
        time.sleep(5)
        self.driver.maximize_window()
        act_title=self.driver.title
        if "OrangeHRM" in act_title:
            assert True
            self.logger.info("************ Home Page Title Test is passed!**************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")

            self.logger.error("************ Home Page Title Test is failed!**************")
            assert False


    def test_login(self,setup):
        self.logger.info("*************** Verifying Login Test *****************")
        self.driver=setup
        self.driver.get(self.baseURL)
        time.sleep(5)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        act_title=self.driver.title
        if "OrangeHRM" in act_title:
            assert True
            self.driver.close()
            self.logger.info("************ Login Test is passed!**************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.error("************ Login Test is failed!**************")
            assert False