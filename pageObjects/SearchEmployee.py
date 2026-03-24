from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchEmployeePage:

    # Locators
    menu_pim_xpath           = "//span[text()='PIM']"
    menu_employee_list_xpath = "//a[text()='Employee List']"

    input_empName_xpath      = "//input[@placeholder='Type for hints...']"
    button_search_xpath      = "//button[@type='submit']"

    result_count_xpath       = "//span[@class='oxd-text oxd-text--span' and contains(text(),'Record')]"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def clickPIMMenu(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, self.menu_pim_xpath))).click()

    def clickEmployeeList(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, self.menu_employee_list_xpath))).click()

    def setEmployeeName(self, name):
        field = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, self.input_empName_xpath)))
        field.clear()
        field.send_keys(name)

    def clickSearch(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, self.button_search_xpath))).click()

    def getResultCountText(self):
        element = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, self.result_count_xpath)))
        return element.text