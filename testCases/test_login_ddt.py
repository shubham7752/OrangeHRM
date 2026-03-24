import pytest
import time
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils


class Test_002_DDT_Login:
    baseURL=ReadConfig.getApplicationURl()
    path=".//testData/logindata.xlsx"

    logger=LogGen.loggen()



    def test_login_ddt(self,setup):
        self.logger.info("************* Test_002_DDT_Login**************")
        self.logger.info("*************** Verifying Login DDT Test *****************")
        self.driver=setup
        self.driver.get(self.baseURL)
        time.sleep(5)

        self.lp=LoginPage(self.driver)

        self.rows=XLUtils.getRowCount(self.path,'Sheet1')
        print("No. of rows in Excel :",self.rows)


        lst_status=[]                 # empty list variable

        for r in range(2,self.rows+1):
            self.user=XLUtils.readData(self.path,'Sheet1',r,1)
            self.password=XLUtils.readData(self.path,'Sheet1',r,2)
            self.exp=XLUtils.readData(self.path,'Sheet1',r,3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title=self.driver.title
            exp_title='Dashboard / nopCommerce administration'

            if act_title==exp_title:
                if self.exp=='pass':
                    self.logger.info('**** Passed ****')
                    self.lp.clickLogout()
                    lst_status.append('pass')

                elif self.exp=='fail':
                    self.logger.info('**** failed ****')
                    self.lp.clickLogout()
                    lst_status.append('fail')

            elif act_title != exp_title:
                if self.exp=='pass':
                    self.logger.info('**** failed ****')
                    self.lp.clickLogout()
                    lst_status.append('fail')

                elif self.exp=='fail':
                    self.logger.info('**** passed ****')
                    self.lp.clickLogout()
                    lst_status.append('pass')

        if "fail" not in lst_status:
            self.logger.info('**** login DDT test case passed ****')
            self.driver.close()
            assert True
        else:
            self.logger.info('**** login DDT test case failed ****')
            self.driver.close()
            assert False

        self.logger.info("************* End of Login DDT Test **************")
        self.logger.info("*************Completed Test_002_DDT_Login **************")



