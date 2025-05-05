from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self,driver):
        self.driver=driver
        self.username_input="user-name"
        self.password_input="password"
        self.login_button="login-button"

    def login(self,username,password):
        self.driver.find_element(By.ID,self.username_input).send_keys(username)
        self.driver.find_element(By.ID, self.password_input).send_keys(password)
        self.driver.find_element(By.ID, self.login_button).click()
