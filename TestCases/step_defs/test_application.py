from pytest_bdd import scenarios, given, when, then, parsers
from PageObjects.HomePage import HomePage
from PageObjects.LoginPage import login
from PageObjects.ModelingPage import ModelingPage
from PageObjects.ProjectPage import ProjectPage
from PageObjects.SimulationPage import SimulationPage

# Scenarios

scenarios('../features/application.feature')


@given(parsers.parse('Login to application "{base_url}" with email_address "{email_address}" and password "{password}"'))
def login_test(browser, base_url, email_address, password):
    browser.get(base_url)
    lp = login(browser)
    hp = HomePage(browser)
    lp.enter_email_address(email_address)
    lp.enter_password(password)
    lp.click_login_button()
    assert hp.validate_home_page_heading_is_present() == True


@when(parsers.parse('user create a project with random name and description "{project_description}"'))
def create_project(browser, project_name, project_description):
    pp = ProjectPage(browser)
    pp.navigate_to_project_page()
    pp.click_new_project_button()
    pp.enter_new_project_name(project_name)
    pp.enter_new_project_description(project_description)
    pp.click_add_button()
    assert pp.validate_project_is_present(project_name) == True


@then(parsers.parse(
    'Add simulation to the created project with name "{simulator_name}" and simulator description "{simulator_description}"'))
def create_simulation(browser, project_name, simulator_name, simulator_description):
    pp = ProjectPage(browser)
    ss = SimulationPage(browser)
    mp = ModelingPage(browser)
    pp.click_on_existing_project_name(project_name)
    pp.click_new_simulation_button_under_project(project_name)
    ss.enter_new_simulation_name(simulator_name)
    ss.enter_new_simulation_description(simulator_description)
    ss.click_new_simulation_next_button()
    assert mp.validate_modeling_page_heading_is_present() == True
