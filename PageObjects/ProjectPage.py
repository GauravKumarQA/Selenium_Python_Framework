from time import sleep

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


class ProjectPage:
    new_project_button_xpath = ".//button//span[text()='new project']"
    new_project_name_field_id = "input-field-name"
    new_project_description_field_id = "textarea-field-nameTextArea"
    new_project_add_button_xpath = ".//button//span[text()='Add']"
    existing_dynamic_project_name = ".//span[text()='PROJECT_NAME']"
    new_simulation_button_under_project = ".//span[text()='PROJECT_NAME']/../../../..//span[text()='new simulation']"

    project_page_url = "https://www.d3a.io/projects"

    def __init__(self, driver):
        self.driver = driver

    def navigate_to_project_page(self):
        self.driver.get(self.project_page_url)
        sleep(5)

    def click_new_project_button(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, self.new_project_button_xpath)))
        self.driver.find_element_by_xpath(self.new_project_button_xpath).click()

    def enter_new_project_name(self, new_project_name):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.ID, self.new_project_name_field_id)))
        self.driver.find_element_by_id(self.new_project_name_field_id).send_keys(new_project_name)

    def enter_new_project_description(self, new_project_description):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.ID, self.new_project_description_field_id)))
        self.driver.find_element_by_id(self.new_project_description_field_id).send_keys(new_project_description)

    def click_add_button(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, self.new_project_add_button_xpath)))
        self.driver.find_element_by_xpath(self.new_project_add_button_xpath).click()

    def click_on_existing_project_name(self, project_name):
        sleep(4)
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, self.existing_dynamic_project_name.replace('PROJECT_NAME', project_name))))
        self.driver.find_element_by_xpath(
            self.existing_dynamic_project_name.replace('PROJECT_NAME', project_name)).click()

    def click_new_simulation_button_under_project(self, project_name):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, self.new_simulation_button_under_project.replace('PROJECT_NAME', project_name))))
        self.driver.find_element_by_xpath(
            self.new_simulation_button_under_project.replace('PROJECT_NAME', project_name)).click()

    def validate_project_is_present(self, project_name):
        try:
            self.driver.find_element_by_xpath(self.existing_dynamic_project_name.replace('PROJECT_NAME', project_name))
        except NoSuchElementException:
            return False
        return True
