from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AddEmployeePage:

    # Locators
    menu_pim_xpath         = "//span[text()='PIM']"
    menu_addEmployee_xpath = "//a[text()='Add Employee']"

    input_firstName_xpath  = "//input[@name='firstName']"
    input_middleName_xpath = "//input[@name='middleName']"
    input_lastName_xpath   = "//input[@name='lastName']"

    input_empId_xpath      = "//input[@class='oxd-input oxd-input--active' and following-sibling::*]"
    button_save_xpath      = "//button[@type='submit']"

    # Toast message after save
    toast_msg_xpath        = "//div[@class='oxd-toast-content']"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def clickPIMMenu(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.menu_pim_xpath))).click()

    def clickAddEmployee(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.menu_addEmployee_xpath))).click()

    def setFirstName(self, firstName):
        field = self.wait.until(EC.presence_of_element_located((By.XPATH, self.input_firstName_xpath)))
        field.clear()
        field.send_keys(firstName)

    def setMiddleName(self, middleName):
        field = self.driver.find_element(By.XPATH, self.input_middleName_xpath)
        field.clear()
        field.send_keys(middleName)

    def setLastName(self, lastName):
        field = self.driver.find_element(By.XPATH, self.input_lastName_xpath)
        field.clear()
        field.send_keys(lastName)

    def clickSave(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_save_xpath))).click()

    def getToastMessage(self):
        toast = self.wait.until(EC.presence_of_element_located((By.XPATH, self.toast_msg_xpath)))
        return toast.text