from selenium.common.exceptions import NoSuchElementException


class SimulationPage:
    new_simulation_name_field_id = "input-field-name"
    new_simulation_description_field_id = "textarea-field-description"
    new_simulation_next_button_xpath = ".//button//span[text()='Next']"

    def __init__(self, driver):
        self.driver = driver

    def enter_new_simulation_name(self, new_simulation_name):
        self.driver.find_element_by_id(self.new_simulation_name_field_id).clear()
        self.driver.find_element_by_id(self.new_simulation_name_field_id).send_keys(new_simulation_name)

    def enter_new_simulation_description(self, new_simulation_description):
        self.driver.find_element_by_id(self.new_simulation_description_field_id).send_keys(new_simulation_description)

    def click_new_simulation_next_button(self):
        self.driver.find_element_by_xpath(self.new_simulation_next_button_xpath).click()

    def validate_modeling_header(self, project_name):
        try:
            self.driver.find_element_by_xpath(
                self.new_simulation_button_under_project.replace('PROJECT_NAME', project_name))
        except NoSuchElementException:
            return False
        return True
