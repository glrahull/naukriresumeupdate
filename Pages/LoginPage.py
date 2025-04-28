import time

from Library import ConfigReader
from selenium.webdriver.common.by import By
from Decorators.Slow import slow_down

class LoginClass:


    def __init__(self,obj):
        global driver
        driver = obj


    @slow_down(5)
    def click_login(self):
        driver.find_element(by= By.ID,value= ConfigReader.fetchelementLocators("Login","login_button_id_name")).click()

    @slow_down(3)
    def enter_username(self,username):
        driver.find_element(by=By.XPATH,value=ConfigReader.fetchelementLocators("Login", "username_xpath")).send_keys(username)

    @slow_down(5)
    def enter_password(self,password):
        driver.find_element(by=By.XPATH,value=ConfigReader.fetchelementLocators("Login", "password_xpath")).send_keys(password)

    @slow_down(5)
    def click_signin(self):
        driver.find_element(by=By.XPATH,value=ConfigReader.fetchelementLocators("Login", "login_button_xpath")).click()

    @slow_down(5)
    def is_login_successful(self):
        try:
             driver.find_element(by=By.XPATH,value=ConfigReader.fetchelementLocators("Login","view_profile_xpath"))
             print("Login Successful ✅")
             return True
        except:
            print("Login Failed ❌")
            return False

    @slow_down(5)
    def view_profile(self):
        driver.find_element(by=By.XPATH,value=ConfigReader.fetchelementLocators("Login","view_profile_xpath")).click()

    @slow_down(5)
    def delete_resume(self):
        driver.find_element(by=By.XPATH,value=ConfigReader.fetchelementLocators("Login","delete_xpath")).click()

    @slow_down(5)
    def delete_confirmation(self):
        driver.find_element(by=By.XPATH,value=ConfigReader.fetchelementLocators("Login","confirm_delete_xpath")).click()
    @slow_down(5)
    def update_resume(self):
        try:
            upload_element = driver.find_element(by=By.ID, value=ConfigReader.fetchelementLocators("Login"))
            upload_element.send_keys(r"C:\Users\rahul\DownloadsRahul Latest CV 18.pdf")
            print("Resume updated successfully ✅")
        except Exception as e:
            print(f"Resume update failed ❌: {e}")

time.sleep(10)



