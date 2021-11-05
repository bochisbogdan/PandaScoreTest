import unittest
import time
from selenium import webdriver as webD
from webdriver_manager.chrome import ChromeDriverManager

from panda import loginOnlyPanda, getFullName, dashboardChangeTheName

class TestPanda(unittest.TestCase):
    def test_loginOnlyPanda(self):
        driver = webD.Chrome(ChromeDriverManager().install())
        email = "xciontx@gmail.com";
        password = "123123123"
        driver, status = loginOnlyPanda(driver=driver, Email= email, Passwors = password)
        self.assertEqual (driver.title, "Pandascore Dashboard")
        self.assertEqual (driver.current_url, "https://app.pandascore.co/dashboard/main")
        self.assertEqual (status, "Your Panda credentials are good!")
        driver.close()
    
    def test_getfullName(self):
        driver = webD.Chrome(ChromeDriverManager().install())
        email = "xciontx@gmail.com";
        password = "123123123"
        driver, status = loginOnlyPanda(driver=driver, Email= email, Passwors = password)
        self.assertEqual (driver.title, "Pandascore Dashboard")
        self.assertEqual (driver.current_url, "https://app.pandascore.co/dashboard/main")
        self.assertEqual (status, "Your Panda credentials are good!")
        driver, fullName = getFullName(driver =driver)
        self.assertEqual (driver.title,"Pandascore Dashboard")
        self.assertEqual (driver.current_url,"https://app.pandascore.co/dashboard/account")
        self.assertNotEqual (fullName,"")
        driver.close()

    def test_dashboardChangeTheName(self):
        driver = webD.Chrome(ChromeDriverManager().install())
        #I know it's not ok to let this here
        email = "xciontx@gmail.com";
        password = "123123123"

        newName = "First_Name Last_Name"
        driver, status = loginOnlyPanda(driver=driver, Email= email, Passwors = password)
        self.assertEqual (driver.title, "Pandascore Dashboard")
        self.assertEqual (driver.current_url, "https://app.pandascore.co/dashboard/main")
        self.assertEqual (status, "Your Panda credentials are good!")
        driver, fullName = getFullName(driver =driver)
        self.assertEqual (driver.title,"Pandascore Dashboard")
        self.assertEqual (driver.current_url,"https://app.pandascore.co/dashboard/account")
        self.assertNotEqual (fullName,"")
        dashboardChangeTheName(driver=driver, fullName=fullName, newName= newName, psw=password)
        driver.close()
        time.sleep(3)
        driver = webD.Chrome(ChromeDriverManager().install())
        driver, status = loginOnlyPanda(driver=driver, Email= email, Passwors = password)
        self.assertEqual (driver.title, "Pandascore Dashboard")
        self.assertEqual (driver.current_url, "https://app.pandascore.co/dashboard/main")
        self.assertEqual (status, "Your Panda credentials are good!")
        driver, fullName = getFullName(driver =driver)
        self.assertEqual (driver.title,"Pandascore Dashboard")
        self.assertEqual (driver.current_url,"https://app.pandascore.co/dashboard/account")
        self.assertEqual (fullName.get_attribute("value"), newName)
        driver.close()

if __name__ == '__main__':
    unittest.main()