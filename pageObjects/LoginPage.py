from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    textbox_username_id = "//input[@name='username']"
    textbox_password_id = "//input[@name='password']"
    button_login_xpath = "//button[@type='submit']"
    link_logout_linktext="Logout"

    def __init__(self,driver):
        self.driver=driver
        self.wait = WebDriverWait(driver, 10)     #  wait added here

    def setUserName(self,username):
        # wait until field is present before interacting
        field = self.wait.until(EC.presence_of_element_located((By.XPATH, self.textbox_username_id)))
        field.clear()
        field.send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(By.XPATH, self.textbox_password_id).clear()
        self.driver.find_element(By.XPATH, self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT,self.link_logout_linktext).click()




