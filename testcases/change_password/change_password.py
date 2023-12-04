from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 

class ChangePasswordTest:
    def __init__(self):
        self.driver = webdriver.Chrome()  # Replace with the appropriate driver for your browser

    def run_test_cases(self):
        self.test_case1()
        self.test_case2()
        # Add more test cases as needed
    def precondition(self):
        '''
        This method is used to perform the precondition steps for the test cases.
        For example, login to the application, navigate to the change password page, etc.
        '''
        self.driver.get("https://school.moodledemo.net/login/index.php")  # Replace with the URL of your application
        # find username box and enter username
        username_input = self.driver.find_element(By.ID, "username")
        username_input.send_keys("teacher")
        # find password box and enter password
        password_input = self.driver.find_element_by_id("password")
        password_input.send_keys("moodle")
        # find login button and click it
        login_button = self.driver.find_element_by_id("loginbtn")
        login_button.click()
        # wait for 0.5 seconds
        self.driver.implicitly_wait(1)
        # find the user menu and click it
        user_menu = self.driver.find_element_by_id("action-menu-toggle-1")
        user_menu.click()
        # find the preferences link and click it
        preferences_link = self.driver.find_element_by_link_text("Preferences")
        preferences_link.click()
        # wait for 0.5 seconds
        self.driver.implicitly_wait(1)
        # find the change password link and click it
        change_password_link = self.driver.find_element_by_link_text("Change Password")
        change_password_link.click()
        # wait for 0.5 seconds
        self.driver.implicitly_wait(1)
        # find the current password input box and enter the current password
    def test_case1(self):
        # Write the code to navigate to the change password page and perform the necessary actions
        # Use self.driver to interact with the web elements
        
        # Write the code to navigate to the change password page and perform the necessary actions
        self.precondition()
        # find the current password input box and enter the current password
        current_password_input = self.driver.find_element_by_id("current_password")
        current_password_input.send_keys("old_password")
        # find the new password input box and enter the new password
        new_password_input = self.driver.find_element_by_id("new_password")
        new_password_input.send_keys("new_password")
        # find the confirm password input box and enter the new password again
        confirm_password_input = self.driver.find_element_by_id("confirm_password")
        confirm_password_input.send_keys("new_password")
        # find the submit button and click it
        submit_button = self.driver.find_element_by_id("submit_button")
        submit_button.click()
        # Add assertions or verifications to validate the result of the test case
        # find the success message and verify it
        success_message = self.driver.find_element_by_id("success_message")
        assert success_message.text == "Password changed successfully"
    def test_case2(self):
        # Write the code for the second test case
        pass
    # Add more test case methods as needed
    def teardown(self):
        self.driver.quit()