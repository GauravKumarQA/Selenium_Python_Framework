Feature: Login to falalana applicatgion
  As a user,
  I want to login to my application,
  So i can create a project with simulation

  Scenario: End to End test
    Given Login to application "https://www.d3a.io/login" with email_address "gaurav.chaudhary440@gmail.com" and password "Gaurav@12"
    When User create a project with random name and description "Project Description 1234"
    Then Add simulation to the created project with name "Simulator123" and simulator description "simulator description 1234"