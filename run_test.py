from testcases.change_password.change_password import ChangePasswordTest

if __name__ == "__main__":
    change_password_test = ChangePasswordTest()
    change_password_test.run_test_cases()
    change_password_test.teardown()