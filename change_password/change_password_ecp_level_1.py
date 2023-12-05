import unittest
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait



class ChangePasswordTestECP(TestCase):
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
        username_input.send_keys("teacher")

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
    def __init__(self):
        self.test_case_data = [
            {
                'name': 'test_case_failed_password_does_not_match',
                "current_password": "moodle",
                "new_password": "1234",
                "confirm_password": "123456",
                'xpath': ['//*[@id="id_error_newpassword1"]', '//*[@id="id_error_newpassword2"]'],
                "message": ["These passwords do not match", "These passwords do not match"]
            },
            {
                'name': 'test_case_failed_empty_new_password_again_box',
                "current_password": "moodle",
                "new_password": "1234",
                "confirm_password": "",
                'xpath': ['//*[@id="id_error_newpassword2"]'],
                "message": ["- Required"]
            },
            {
                'name': 'test_case_failed_empty_new_password_box',
                "current_password": "moodle",
                "new_password": "",
                "confirm_password": "abc",
                'xpath': ['//*[@id="id_error_newpassword1"]'],
                "message": ["- Required"]
            },
            {
                'name': 'test_case_failed_invalid_current_password',
                "current_password": "admin",
                "new_password": "1234",
                "confirm_password": "1234",
                'xpath': ['//*[@id="id_error_password"]'],
                "message": ["Invalid login, please try again"]
            },
            {
                'name': 'test_case_failed_empty_current_password',
                "current_password": "",
                "new_password": "1234",
                "confirm_password": "1234",
                'xpath': ['//*[@id="id_error_password"]'],
                "message": ["- Required"]
            }
        ]
    def run_all(self):
        for test_case in self.test_case_data:
            self.setUp()
            # find the current password input box and enter the current password
            current_password_input = self.driver.find_element(By.XPATH, '//*[@id="id_password"]')
            current_password_input.send_keys(test_case["current_password"])

            # find the new password input box and enter the new password
            new_password_input = self.driver.find_element(By.XPATH, '//*[@id="id_newpassword1"]')
            new_password_input.send_keys(test_case["new_password"])
            
            # find the confirm password input box and enter the new password again
            confirm_password_input = self.driver.find_element(By.XPATH, '//*[@id="id_newpassword2"]')
            confirm_password_input.send_keys(test_case["confirm_password"])
            
            # find the submit button and click it
            submit_button = self.driver.find_element(By.XPATH, '//*[@id="id_submitbutton"]')
            submit_button.click()

            for xpath, message in zip(test_case["xpath"], test_case["message"]):
                error_message = self.driver.find_element(By.XPATH, xpath)
                assert error_message.text == message        
            self.tearDown()
if __name__ == "__main__":
    ChangePasswordTestECP().run_all()