from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


class login:
    email_input_field_id = "email"
    password_input_field_id = "password"
    login_button_xpath = ".//button//span[text()='Login']"
    home_button_heading_xpath = ".//h1[text()='Home']"

    def __init__(self, driver):
        self.driver = driver

    def enter_email_address(self, email_address):
        self.driver.find_element_by_id(self.email_input_field_id).send_keys(email_address)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_input_field_id).send_keys(password)

    def click_login_button(self):
        self.driver.find_element_by_xpath(self.login_button_xpath).click()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, self.home_button_heading_xpath)))
