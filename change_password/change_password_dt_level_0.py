import unittest
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait



class ChangePasswordTestDT(TestCase):
    def setUp(self):
        '''
        Perform:
        1. Login to the application in teacher role
        2. Navigate to the user profile dropdown menu
        3. Navigate to the preferences page
        4. Navigate to the change password page
        '''
        self.driver = webdriver.Chrome()
        self.driver.get("https://school.moodledemo.net/login/index.php")

        # find username box and enter username
        username_input = self.driver.find_element(By.ID, "username")
        username_input.send_keys("student")

        # find password box and enter password
        password_input = self.driver.find_element(By.ID,"password")
        password_input.send_keys("moodle")

        # find login button and click it
        login_button = self.driver.find_element(By.ID,"loginbtn")
        login_button.click()

        # wait until the page is loaded
        wait = WebDriverWait(self.driver, 10)
        _ = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="user-menu-toggle"]')))

        # find the user menu and click it
        user_menu = self.driver.find_element(By.XPATH, '//*[@id="user-menu-toggle"]')
        user_menu.click()

        _ = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Preferences')))
        # find the preferences link and click it
        preferences_link = self.driver.find_element(By.LINK_TEXT,"Preferences")
        preferences_link.click()

        _ = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Change password')))

        # find the change password link and click it
        change_password_link = self.driver.find_element(By.LINK_TEXT,"Change password")
        change_password_link.click()

    def tearDown(self):
        self.driver.close()

    def test_case_success(self):
        # find the current password input box and enter the current password
        current_password_input = self.driver.find_element(By.XPATH, '//*[@id="id_password"]')
        current_password_input.send_keys("moodle")

        # find the new password input box and enter the new password
        new_password_input = self.driver.find_element(By.XPATH, '//*[@id="id_newpassword1"]')
        new_password_input.send_keys("abc")
        
        # find the confirm password input box and enter the new password again
        confirm_password_input = self.driver.find_element(By.XPATH, '//*[@id="id_newpassword2"]')
        confirm_password_input.send_keys("abc")
        
        # find the submit button and click it
        submit_button = self.driver.find_element(By.XPATH, '//*[@id="id_submitbutton"]')
        submit_button.click()
        
        wait = WebDriverWait(self.driver, 10)
        _ = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/div/section/div/div[2]/form/button')))
        # Add assertions or verifications to validate the result of the test case
        # find the success message and verify it
        success_message = self.driver.find_element(By.XPATH, '//*[@id="notice"]')
        assert success_message.text == "Password has been changed"
        # change password the old password
        continue_button = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/div/section/div/div[2]/form/button')

        continue_button.click()

        _ = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Change password')))

        # find the change password link and click it
        change_password_link = self.driver.find_element(By.LINK_TEXT,"Change password")
        change_password_link.click()

        # find the current password input box and enter the current password
        current_password_input = self.driver.find_element(By.XPATH, '//*[@id="id_password"]')
        current_password_input.send_keys("abc")

        # find the new password input box and enter the new password
        new_password_input = self.driver.find_element(By.XPATH, '//*[@id="id_newpassword1"]')
        new_password_input.send_keys("moodle")
        
        # find the confirm password input box and enter the new password again
        confirm_password_input = self.driver.find_element(By.XPATH, '//*[@id="id_newpassword2"]')
        confirm_password_input.send_keys("moodle")
        
        # find the submit button and click it
        submit_button = self.driver.find_element(By.XPATH, '//*[@id="id_submitbutton"]')
        submit_button.click()

        _ = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/div/section/div/div[2]/form/button')))
        
        continue_button = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/div/section/div/div[2]/form/button')
        continue_button.click()
    def test_case_failed_password_does_not_match(self):
        # find the current password input box and enter the current password
        current_password_input = self.driver.find_element(By.XPATH, '//*[@id="id_password"]')
        current_password_input.send_keys("moodle")

        # find the new password input box and enter the new password
        new_password_input = self.driver.find_element(By.XPATH, '//*[@id="id_newpassword1"]')
        new_password_input.send_keys("1234")
        
        # find the confirm password input box and enter the new password again
        confirm_password_input = self.driver.find_element(By.XPATH, '//*[@id="id_newpassword2"]')
        confirm_password_input.send_keys("123456")
        
        # find the submit button and click it
        submit_button = self.driver.find_element(By.XPATH, '//*[@id="id_submitbutton"]')
        submit_button.click()
        
        # Add assertions or verifications to validate the result of the test case
        # find the success message and verify it
        error_message_1 = self.driver.find_element(By.XPATH, '//*[@id="id_error_newpassword1"]')
        assert error_message_1.text == "These passwords do not match"
        error_message_2 = self.driver.find_element(By.XPATH, '//*[@id="id_error_newpassword2"]')
        assert error_message_2.text == "These passwords do not match"

    def test_case_failed_empty_new_password_again_box(self):
        # find the current password input box and enter the current password
        current_password_input = self.driver.find_element(By.XPATH, '//*[@id="id_password"]')
        current_password_input.send_keys("moodle")

        # find the new password input box and enter the new password
        new_password_input = self.driver.find_element(By.XPATH, '//*[@id="id_newpassword1"]')
        new_password_input.send_keys("1234")
        
        # find the confirm password input box and enter the new password again
        confirm_password_input = self.driver.find_element(By.XPATH, '//*[@id="id_newpassword2"]')
        confirm_password_input.send_keys("")
        
        # find the submit button and click it
        submit_button = self.driver.find_element(By.XPATH, '//*[@id="id_submitbutton"]')
        submit_button.click()
        
        # Add assertions or verifications to validate the result of the test case
        # find the error message and verify it
        error_message_2 = self.driver.find_element(By.XPATH, '//*[@id="id_error_newpassword2"]')
        assert error_message_2.text == "- Required"

    def test_case_failed_empty_new_password_box(self):
        # find the current password input box and enter the current password
        current_password_input = self.driver.find_element(By.XPATH, '//*[@id="id_password"]')
        current_password_input.send_keys("moodle")

        # find the new password input box and enter the new password
        new_password_input = self.driver.find_element(By.XPATH, '//*[@id="id_newpassword1"]')
        new_password_input.send_keys("")
        
        # find the confirm password input box and enter the new password again
        confirm_password_input = self.driver.find_element(By.XPATH, '//*[@id="id_newpassword2"]')
        confirm_password_input.send_keys("abc")
        
        # find the submit button and click it
        submit_button = self.driver.find_element(By.XPATH, '//*[@id="id_submitbutton"]')
        submit_button.click()
        
        # Add assertions or verifications to validate the result of the test case
        # find the error message and verify it
        error_message_2 = self.driver.find_element(By.XPATH, '//*[@id="id_error_newpassword1"]')
        assert error_message_2.text == "- Required"

    def test_case_failed_invalid_current_password_valid_confirm_password(self):
        # find the current password input box and enter the current password
        current_password_input = self.driver.find_element(By.XPATH, '//*[@id="id_password"]')
        current_password_input.send_keys("admin")

        # find the new password input box and enter the new password
        new_password_input = self.driver.find_element(By.XPATH, '//*[@id="id_newpassword1"]')
        new_password_input.send_keys("1234")
        
        # find the confirm password input box and enter the new password again
        confirm_password_input = self.driver.find_element(By.XPATH, '//*[@id="id_newpassword2"]')
        confirm_password_input.send_keys("1234")
        
        # find the submit button and click it
        submit_button = self.driver.find_element(By.XPATH, '//*[@id="id_submitbutton"]')
        submit_button.click()
        
        # Add assertions or verifications to validate the result of the test case
        # find the error message and verify it
        error_message_2 = self.driver.find_element(By.XPATH, '//*[@id="id_error_password"]')
        assert error_message_2.text == "Invalid login, please try again"

    def test_case_failed_invalid_current_password_invalid_confirm_password(self):
        # find the current password input box and enter the current password
        current_password_input = self.driver.find_element(By.XPATH, '//*[@id="id_password"]')
        current_password_input.send_keys("admin")

        # find the new password input box and enter the new password
        new_password_input = self.driver.find_element(By.XPATH, '//*[@id="id_newpassword1"]')
        new_password_input.send_keys("1234")
        
        # find the confirm password input box and enter the new password again
        confirm_password_input = self.driver.find_element(By.XPATH, '//*[@id="id_newpassword2"]')
        confirm_password_input.send_keys("123456")
        
        # find the submit button and click it
        submit_button = self.driver.find_element(By.XPATH, '//*[@id="id_submitbutton"]')
        submit_button.click()
        
        # Add assertions or verifications to validate the result of the test case
        # find the error message and verify it
        error_message_2 = self.driver.find_element(By.XPATH, '//*[@id="id_error_password"]')
        assert error_message_2.text == "Invalid login, please try again"

    def test_case_failed_invalid_current_password_empty_confirm_password(self):
        # find the current password input box and enter the current password
        current_password_input = self.driver.find_element(By.XPATH, '//*[@id="id_password"]')
        current_password_input.send_keys("admin")

        # find the new password input box and enter the new password
        new_password_input = self.driver.find_element(By.XPATH, '//*[@id="id_newpassword1"]')
        new_password_input.send_keys("1234")
        
        # find the confirm password input box and enter the new password again
        confirm_password_input = self.driver.find_element(By.XPATH, '//*[@id="id_newpassword2"]')
        confirm_password_input.send_keys("")
        
        # find the submit button and click it
        submit_button = self.driver.find_element(By.XPATH, '//*[@id="id_submitbutton"]')
        submit_button.click()
        
        # Add assertions or verifications to validate the result of the test case
        # find the error message and verify it
        error_message_2 = self.driver.find_element(By.XPATH, '//*[@id="id_error_newpassword2"]')
        assert error_message_2.text == "- Required"

    def test_case_failed_invalid_current_password_empty_new_password_box(self):
        # find the current password input box and enter the current password
        current_password_input = self.driver.find_element(By.XPATH, '//*[@id="id_password"]')
        current_password_input.send_keys("admin")

        # find the new password input box and enter the new password
        new_password_input = self.driver.find_element(By.XPATH, '//*[@id="id_newpassword1"]')
        new_password_input.send_keys("")
        
        # find the confirm password input box and enter the new password again
        confirm_password_input = self.driver.find_element(By.XPATH, '//*[@id="id_newpassword2"]')
        confirm_password_input.send_keys("123456")
        
        # find the submit button and click it
        submit_button = self.driver.find_element(By.XPATH, '//*[@id="id_submitbutton"]')
        submit_button.click()
        
        # Add assertions or verifications to validate the result of the test case
        # find the error message and verify it
        error_message_2 = self.driver.find_element(By.XPATH, '//*[@id="id_error_newpassword1"]')
        assert error_message_2.text == "- Required"

    def test_case_failed_empty_current_password_non_empty_new_password_valid_confirm_password(self):
        # find the current password input box and enter the current password
        current_password_input = self.driver.find_element(By.XPATH, '//*[@id="id_password"]')
        current_password_input.send_keys("")

        # find the new password input box and enter the new password
        new_password_input = self.driver.find_element(By.XPATH, '//*[@id="id_newpassword1"]')
        new_password_input.send_keys("1234")
        
        # find the confirm password input box and enter the new password again
        confirm_password_input = self.driver.find_element(By.XPATH, '//*[@id="id_newpassword2"]')
        confirm_password_input.send_keys("1234")
        
        # find the submit button and click it
        submit_button = self.driver.find_element(By.XPATH, '//*[@id="id_submitbutton"]')
        submit_button.click()
        
        # Add assertions or verifications to validate the result of the test case
        # find the error message and verify it
        error_message_2 = self.driver.find_element(By.XPATH, '//*[@id="id_error_password"]')
        assert error_message_2.text == "- Required"

    def test_case_failed_empty_current_password_non_empty_new_password_invalid_confirm_password(self):
        # find the current password input box and enter the current password
        current_password_input = self.driver.find_element(By.XPATH, '//*[@id="id_password"]')
        current_password_input.send_keys("")

        # find the new password input box and enter the new password
        new_password_input = self.driver.find_element(By.XPATH, '//*[@id="id_newpassword1"]')
        new_password_input.send_keys("1234")
        
        # find the confirm password input box and enter the new password again
        confirm_password_input = self.driver.find_element(By.XPATH, '//*[@id="id_newpassword2"]')
        confirm_password_input.send_keys("123456")
        
        # find the submit button and click it
        submit_button = self.driver.find_element(By.XPATH, '//*[@id="id_submitbutton"]')
        submit_button.click()
        
        # Add assertions or verifications to validate the result of the test case
        # find the error message and verify it
        error_message_2 = self.driver.find_element(By.XPATH, '//*[@id="id_error_password"]')
        assert error_message_2.text == "- Required"

    def test_case_failed_empty_current_password_non_empty_new_password_empty_confirm_password(self):
        # find the current password input box and enter the current password
        current_password_input = self.driver.find_element(By.XPATH, '//*[@id="id_password"]')
        current_password_input.send_keys("")

        # find the new password input box and enter the new password
        new_password_input = self.driver.find_element(By.XPATH, '//*[@id="id_newpassword1"]')
        new_password_input.send_keys("1234")
        
        # find the confirm password input box and enter the new password again
        confirm_password_input = self.driver.find_element(By.XPATH, '//*[@id="id_newpassword2"]')
        confirm_password_input.send_keys("")
        
        # find the submit button and click it
        submit_button = self.driver.find_element(By.XPATH, '//*[@id="id_submitbutton"]')
        submit_button.click()
        
        # Add assertions or verifications to validate the result of the test case
        # find the error message and verify it
        error_message_2 = self.driver.find_element(By.XPATH, '//*[@id="id_error_password"]')
        assert error_message_2.text == "- Required"

    def test_case_failed_empty_current_password_empty_new_password(self):
        # find the current password input box and enter the current password
        current_password_input = self.driver.find_element(By.XPATH, '//*[@id="id_password"]')
        current_password_input.send_keys("")

        # find the new password input box and enter the new password
        new_password_input = self.driver.find_element(By.XPATH, '//*[@id="id_newpassword1"]')
        new_password_input.send_keys("")
        
        # find the confirm password input box and enter the new password again
        confirm_password_input = self.driver.find_element(By.XPATH, '//*[@id="id_newpassword2"]')
        confirm_password_input.send_keys("12")
        
        # find the submit button and click it
        submit_button = self.driver.find_element(By.XPATH, '//*[@id="id_submitbutton"]')
        submit_button.click()
        
        # Add assertions or verifications to validate the result of the test case
        # find the error message and verify it
        error_message_2 = self.driver.find_element(By.XPATH, '//*[@id="id_error_password"]')
        assert error_message_2.text == "- Required"
if __name__ == "__main__":
    unittest.main()