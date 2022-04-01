import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time


@pytest.fixture()
def setUp():
    global name, driver, address, mobile, pincode, email, password, password2
    name = input("Enter name : ")
    address = input("Enter address : ")
    pincode = input("Enter pincode: ")
    mobile = input("Enter mobileNo: ")
    email = input("Enter emailId: ")
    password = input("Enter password: ")
    password2 = input("Confirm password: ")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    print("Test case started")
    driver.maximize_window()
    yield
    time.sleep(8)
    driver.close()

def test_form(setUp):
    driver.get("https://iprimedtraining.herokuapp.com/userdata.php")
    driver.find_element_by_name("name").send_keys(name)
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[2]/td[2]/input[1]").click()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[3]/td[2]/select/option[4]").click()
    time.sleep(1)
    driver.find_element_by_name("Address").send_keys(address)
    time.sleep(1)
    driver.find_element_by_name("Pincode").send_keys(pincode)
    time.sleep(1)
    driver.find_element_by_name("Mobile").send_keys(mobile)
    time.sleep(1)
    driver.find_element_by_name("Email").send_keys(email)
    time.sleep(1)
    driver.find_element_by_name("pass").send_keys(password)
    time.sleep(1)
    driver.find_element_by_name("cnfpass").send_keys(password2)
    time.sleep(1)
    driver.find_element_by_name("fcheckbox").click()
    time.sleep(1)
    driver.find_element_by_name("subbtn").click()

    #Right Click functionality
    time.sleep(1)
    action = ActionChains(driver)
    action.context_click(driver.find_element_by_name("Pincode"))
    time.sleep(1)
    action.perform()
    time.sleep(5)