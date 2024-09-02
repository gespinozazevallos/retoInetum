from behave import given, when, then
from playwright.sync_api import Page
import random

@given('I am on the login page')
def step_given_i_am_on_the_login_page(context):
    context.page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

@when('I login with username "{username}" and password "{password}"')
def step_when_i_login_with_username_and_password(context, username, password):
    context.page.fill("input[name='username']", username)
    context.page.fill("input[name='password']", password)
    context.page.click("button[type='submit']")

@when('I add a new employee with name "{employee_name}"')
def step_when_i_add_a_new_employee(context, employee_name):
    random_number = random.randint(1, 9999)
    employee_name_with_number = f'Test_{employee_name}_{random_number}'
    context.employee_name_with_number = employee_name_with_number  
    context.page.click("span:has-text('Admin')")
    context.page.click("button:has-text('Add')")
    context.page.click("div.oxd-select-text--active")
    context.page.click('div.oxd-select-dropdown div:has-text("Admin")')
    context.page.fill('div.oxd-autocomplete-wrapper input[placeholder="Type for hints..."]', employee_name)
    context.page.wait_for_selector('div.oxd-autocomplete-dropdown', state='visible')
    context.page.click(f'div.oxd-autocomplete-dropdown div:has-text("{employee_name}")')
    context.page.click('div.oxd-select-text--active:has-text("-- Select --")')
    context.page.click('div.oxd-select-dropdown div:has-text("Enabled")')
    context.page.wait_for_selector('input.oxd-input.oxd-input--active[autocomplete="off"]', state='visible')
    context.page.fill('input.oxd-input.oxd-input--active[autocomplete="off"]', employee_name_with_number)

@when('I add a password "{password}"')
def step_when_i_add_a_password(context, password):
    context.page.fill('div.oxd-input-group input.oxd-input.oxd-input--active[type="password"]', password)
    context.page.fill('div.oxd-grid-item div.oxd-input-group input.oxd-input.oxd-input--active[type="password"]', password)
    context.page.click('button[type="submit"]:has-text("Save")')
    context.page.wait_for_timeout(5000)

@then('I should see the new employee in the employee list')
def step_then_i_should_see_in_the_employee_list(context):
    employee_name_with_number = getattr(context, 'employee_name_with_number', None)
    
    if not employee_name_with_number:
        raise ValueError("Employee name with number is not set in the context.")
    
    context.page.click("span:has-text('Admin')")
    context.page.wait_for_selector(f"text={employee_name_with_number}", state='visible') 
    assert context.page.locator(f"text={employee_name_with_number}").is_visible()
