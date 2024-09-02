Feature: Employee Management

  Scenario: Add a new employee
    Given I am on the login page
    When I login with username "Admin" and password "admin123"
    And I add a new employee with name "lewis"
    And I add a password "Testing21"
    Then I should see the new employee in the employee list
