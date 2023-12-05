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
    def test_upload_file(self):
        # implicit wait for 10 seconds
        self.driver.implicitly_wait(10)

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        self.driver.implicitly_wait(10)

        # Locate the file input element and the drop box element
        drop_box = self.driver.find_element(By.XPATH, "//*[starts-with(@id,'yui_3_18_1_1')]/div[1]/div[2]/div/div")
        # Path to the file you want to upload
        drop_box.click()
        
        upload_a_file_button = self.driver.find_element(By.LINK_TEXT, "Upload a file")
        upload_a_file_button.click()
        
        import os
        file_path =  "__init__.py"
        absolute_file_path = os.path.abspath(file_path)
        print(absolute_file_path)
        file_input = self.driver.find_element(By.CSS_SELECTOR, "input[type='file']")
        file_input.send_keys(absolute_file_path)
        self.driver.implicitly_wait(30)

        
        wait = WebDriverWait(self.driver, 10)
        _ = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[7]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div/button')))
        upload_this_file_button = self.driver.find_element(By.XPATH, '/html/body/div[7]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div/button')
        upload_this_file_button.click()
        self.driver.implicitly_wait(30)

        _ = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="id_submitbutton"]')))

        save_changes_button = self.driver.find_element(By.XPATH, '//*[@id="id_submitbutton"]')
        save_changes_button.click()
        self.driver.implicitly_wait(30)

        
        
        
if __name__ == "__main__":
    unittest.main()