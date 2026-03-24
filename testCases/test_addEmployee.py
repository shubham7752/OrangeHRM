import pytest
import os
from pageObjects.LoginPage import LoginPage
from pageObjects.AddEmployee import AddEmployeePage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test_003_AddEmployee:
    baseURL  = ReadConfig.getApplicationURl()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_addEmployee(self, setup):
        self.logger.info("************* Test_003_AddEmployee **************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        wait = WebDriverWait(self.driver, 10)

        # Step 1: Login
        self.logger.info("*** Logging in ***")
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        # Wait for dashboard after login
        try:
            wait.until(EC.url_contains("dashboard"))
            self.logger.info("*** Login successful, dashboard loaded ***")
        except:
            self.driver.save_screenshot(".\\Screenshots\\test_addEmployee_login_failed.png")
            self.logger.error("*** Login failed - dashboard not loaded ***")
            self.driver.close()
            assert False, "Login failed - dashboard not loaded"

        # Step 2: Navigate to Add Employee
        self.logger.info("*** Navigating to Add Employee ***")
        try:
            ap = AddEmployeePage(self.driver)
            ap.clickPIMMenu()
            ap.clickAddEmployee()
            self.logger.info("*** Navigated to Add Employee page ***")
        except:
            self.driver.save_screenshot(".\\Screenshots\\test_addEmployee_navigation_failed.png")
            self.logger.error("*** Navigation to Add Employee failed ***")
            self.driver.close()
            assert False, "Navigation to Add Employee page failed"

        # Step 3: Fill details
        self.logger.info("*** Filling Employee Details ***")
        try:
            ap.setFirstName("John")
            ap.setMiddleName("K")
            ap.setLastName("Doe")
            self.logger.info("*** Employee details filled ***")
        except:
            self.driver.save_screenshot(".\\Screenshots\\test_addEmployee_form_failed.png")
            self.logger.error("*** Filling employee details failed ***")
            self.driver.close()
            assert False, "Filling employee form failed"

        # Step 4: Save
        self.logger.info("*** Saving Employee ***")
        try:
            ap.clickSave()
            wait.until(EC.url_contains("personal-details"))
            self.logger.info("*** Save successful ***")
        except:
            self.driver.save_screenshot(".\\Screenshots\\test_addEmployee_save_failed.png")
            self.logger.error("*** Save failed ***")
            self.driver.close()
            assert False, "Save employee failed"

        # Step 5: Verify
        act_title = self.driver.title
        if "Personal Details" in act_title:
            self.logger.info("*** Add Employee Test PASSED ***")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_addEmployee_verify_failed.png")
            self.logger.error("*** Add Employee Test FAILED ***")
            self.driver.close()
            assert False