import pytest
import time
import os
from pageObjects.LoginPage import LoginPage
from pageObjects.SearchEmployee import SearchEmployeePage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test_004_SearchEmployee:
    baseURL  = ReadConfig.getApplicationURl()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_searchEmployee(self, setup):
        self.logger.info("************* Test_004_SearchEmployee **************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        # Step 1: Login
        self.logger.info("*** Logging in ***")
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(3)

        # Step 2: Navigate to PIM > Employee List
        self.logger.info("*** Navigating to Employee List ***")
        self.sp = SearchEmployeePage(self.driver)
        self.sp.clickPIMMenu()
        time.sleep(2)
        self.sp.clickEmployeeList()
        time.sleep(3)

        # Step 3: Search for employee by name
        self.logger.info("*** Searching for employee: John ***")
        self.sp.setEmployeeName("John")
        time.sleep(2)
        self.sp.clickSearch()
        time.sleep(3)

        # Step 4: Verify results
        result_text = self.sp.getResultCountText()
        self.logger.info(f"*** Result: {result_text} ***")

        if "Record" in result_text:
            self.logger.info("*** Search Employee Test PASSED ***")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(
                ".\\Screenshots\\test_searchEmployee_failed.png")
            self.logger.error("*** Search Employee Test FAILED ***")
            self.driver.close()
            assert False