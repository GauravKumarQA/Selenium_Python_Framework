from selenium.common.exceptions import NoSuchElementException


class HomePage:
    home_page_heading_xpath = ".//h1[text()='Home']"

    def __init__(self, driver):
        self.driver = driver

    def validate_home_page_heading_is_present(self):
        try:
            self.driver.find_element_by_xpath(self.home_page_heading_xpath)
        except NoSuchElementException:
            return False
        return True
