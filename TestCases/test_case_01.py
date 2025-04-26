import time

import pytest
from Pages import LoginPage
from Base import InitiateDriver
from DataGenerate import DataGen


@pytest.mark.parametrize('data', DataGen.dataGenerator())
def test_combined(data):
    # Run the first test case
    driver = InitiateDriver.startBrowser()

    # Test login functionality

    login = LoginPage.LoginClass(driver)
    login.click_login()
    login.enter_username(data[0])
    login.enter_password(data[1])
    login.click_signin()
    login.is_login_successful()
    login.view_profile()
    login.delete_resume()
    login.delete_confirmation()
    login.update_resume()

time.sleep(8)


