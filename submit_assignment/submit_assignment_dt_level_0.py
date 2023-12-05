import unittest
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains


class SubmitAssignmentTestDT(TestCase):
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

        self.driver.get("https://school.moodledemo.net/mod/assign/view.php?id=1008&action=editsubmission")
    def tearDown(self):
        self.driver.close()
    def test(self):
        # implicit wait for 10 seconds
        self.driver.implicitly_wait(10)

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        self.driver.implicitly_wait(10)

        # Locate the file input element and the drop box element
        drop_box = self.driver.find_element(By.CLASS_NAME, "fa fa-arrow-circle-o-down fa-3x m-auto")  # Replace with your drop box element's locator
        # Path to the file you want to upload
        drop_box.click()
        
        file_path = "__init__.py"

        # Use ActionChains to perform drag and drop
        action = ActionChains(self.driver)
        action.drag_and_drop(file_path, drop_box).perform()
if __name__ == "__main__":
    unittest.main()