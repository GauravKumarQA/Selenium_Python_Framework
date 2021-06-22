from selenium.common.exceptions import NoSuchElementException


class ModelingPage:
    modeling_page_heading_xpath = ".//h1[text()='Modelling']"

    def __init__(self, driver):
        self.driver = driver

    def validate_modeling_page_heading_is_present(self):
        try:
            self.driver.find_element_by_xpath(self.modeling_page_heading_xpath)
        except NoSuchElementException:
            return False
        return True
