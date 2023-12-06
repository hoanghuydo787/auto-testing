import unittest
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains


class SubmitAssignmentTestUC(TestCase):
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
                            
        self.driver.get("https://school.moodledemo.net/mod/assign/view.php?id=1188&action=editsubmission")

    def tearDown(self):
        self.driver.close()

    def test_upload_file_invalid_type(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        wait = WebDriverWait(self.driver, 15)

        _ = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@title='Add...']")))
        drop_box = self.driver.find_element(By.XPATH, "//a[@title='Add...']")
        drop_box.click()

        _ = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Upload a file")))
        upload_a_file_button = self.driver.find_element(By.LINK_TEXT, "Upload a file")
        upload_a_file_button.click()
        
        import os
        file_path = "data\\invalid_type_invalid_size.zip"
        absolute_file_path = os.path.abspath(file_path)
        print(absolute_file_path)
        
        _ = wait.until(EC.element_to_be_clickable((By.NAME, "repo_upload_file")))
        choose_file_button = self.driver.find_element(By.NAME, "repo_upload_file")        
        choose_file_button.send_keys(absolute_file_path)
        self.driver.implicitly_wait(10)

        _ = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Upload this file']")))
        upload_this_file_button = self.driver.find_element(By.XPATH, "//button[text()='Upload this file']")
        upload_this_file_button.click()

        import time
        time.sleep(5)

        # class="fp-msg-text" id="fp-msg-labelledby"
        # message = self.driver.find_element(By.CLASS_NAME, "fp-msg-text")
        message = self.driver.find_element(By.CLASS_NAME, "moodle-exception-message")
        # assert message.text == 'The file invalid_type_invalid_size.zip is too large. The maximum size you can upload is 1 MB.'
        assert message.text == 'Archive (ZIP) filetype cannot be accepted.'
        # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # _ = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="id_submitbutton"]')))
        # save_changes_button = self.driver.find_element(By.XPATH, '//*[@id="id_submitbutton"]')
        # save_changes_button.click()
    def test_upload_file_valid_type_invalid_size(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        wait = WebDriverWait(self.driver, 15)

        _ = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@title='Add...']")))
        drop_box = self.driver.find_element(By.XPATH, "//a[@title='Add...']")
        drop_box.click()

        _ = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Upload a file")))
        upload_a_file_button = self.driver.find_element(By.LINK_TEXT, "Upload a file")
        upload_a_file_button.click()
        
        import os
        file_path = "data\\valid_type_invalid_size.pdf"
        absolute_file_path = os.path.abspath(file_path)
        print(absolute_file_path)
        
        _ = wait.until(EC.element_to_be_clickable((By.NAME, "repo_upload_file")))
        choose_file_button = self.driver.find_element(By.NAME, "repo_upload_file")        
        choose_file_button.send_keys(absolute_file_path)
        self.driver.implicitly_wait(10)

        _ = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Upload this file']")))
        upload_this_file_button = self.driver.find_element(By.XPATH, "//button[text()='Upload this file']")
        upload_this_file_button.click()

        import time
        time.sleep(5)

        # class="fp-msg-text" id="fp-msg-labelledby"
        # message = self.driver.find_element(By.CLASS_NAME, "fp-msg-text")
        message = self.driver.find_element(By.CLASS_NAME, "moodle-exception-message")
        assert message.text == 'The file valid_type_invalid_size.pdf is too large. The maximum size you can upload is 1 MB.'
        # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # _ = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="id_submitbutton"]')))
        # save_changes_button = self.driver.find_element(By.XPATH, '//*[@id="id_submitbutton"]')
        # save_changes_button.click()

    def test_upload_file_valid_type_valid_size(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        wait = WebDriverWait(self.driver, 15)

        _ = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@title='Add...']")))
        drop_box = self.driver.find_element(By.XPATH, "//a[@title='Add...']")
        drop_box.click()

        _ = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Upload a file")))
        upload_a_file_button = self.driver.find_element(By.LINK_TEXT, "Upload a file")
        upload_a_file_button.click()
        
        import os
        file_path = "data\\valid_type_valid_size.pdf"
        absolute_file_path = os.path.abspath(file_path)
        print(absolute_file_path)
        
        _ = wait.until(EC.element_to_be_clickable((By.NAME, "repo_upload_file")))
        choose_file_button = self.driver.find_element(By.NAME, "repo_upload_file")        
        choose_file_button.send_keys(absolute_file_path)
        self.driver.implicitly_wait(10)

        _ = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Upload this file']")))
        upload_this_file_button = self.driver.find_element(By.XPATH, "//button[text()='Upload this file']")
        upload_this_file_button.click()

        import time
        time.sleep(5)

        # class="fp-msg-text" id="fp-msg-labelledby"
        # message = self.driver.find_element(By.CLASS_NAME, "fp-msg-text")
        # message = self.driver.find_element(By.CLASS_NAME, "moodle-exception-message")
        # assert message.text == 'The file valid_type_invalid_size.pdf is too large. The maximum size you can upload is 1 MB.'
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        _ = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="id_submitbutton"]')))
        save_changes_button = self.driver.find_element(By.XPATH, '//*[@id="id_submitbutton"]')
        save_changes_button.click()

        submission_status = self.driver.find_element(By.XPATH, '//*[@id="region-main"]/div[2]/div[2]/div/div/table/tbody/tr[1]/td')        
        assert submission_status.text == 'Submitted for grading'
        # print("success")
        # time.sleep(30)
if __name__ == "__main__":
    unittest.main()