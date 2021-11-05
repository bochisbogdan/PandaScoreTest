import time
from logging import exception

from selenium import webdriver as webD
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


def loginOnlyPanda(driver : webD, Passwors: str, Email: str):
    base_url = "https://app.pandascore.co/login"

    driver.get(base_url)

    time.sleep(5)
    button = driver.find_element(By.XPATH,"//input[@value=\"Login\"]")
    
    email = driver.find_element(By.NAME,"email")
    password = driver.find_element(By.NAME,"password")
    
    email.send_keys(Email)
    password.send_keys(Passwors)

    button.submit()

    time.sleep(5)

    status = "Your Panda credentials are good!"
    try:
        message  = driver.find_element(By.CLASS_NAME,"my-alert-error")
        status = message.text;

    except Exception:
        pass
        
    return driver, status


def getFullName(driver: webD):
    link = driver.find_element(By.LINK_TEXT,"Account")
    driver.execute_script("arguments[0].click();",link)
    time.sleep(10)
    
    try:
        fullName = driver.find_element(By.XPATH,"//span[contains(text(),'Name')]/following-sibling::*[1]")
    except Exception:
        print("Something'g rong!")
    
    return driver , fullName;


def dashboardChangeTheName(driver: webD, fullName: any, newName: str, psw: str):
    
    button = driver.find_element(By.CLASS_NAME,"btn-panda")
    
    password = driver.find_element(By.XPATH,"//span[contains(text(),'Current password')]/following-sibling::*[1]")
    password.send_keys(psw)

    fullName.send_keys(Keys.BACKSPACE)
    for i in str(fullName):
        fullName.send_keys(Keys.BACKSPACE)
    
    fullName.send_keys(newName)
    try:
        button.submit()
    except Exception:
        print("Something'g rong!")
    
    time.sleep(5)


def logOut(driver: webD):
    logOut_button = driver.find_element(By.LINK_TEXT,"Account")
    driver.execute_script("arguments[0].click();",logOut_button)
    time.sleep(5)
    driver.close()
    return driver


def startBrowser():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_prefs = {}
    chrome_options.experimental_options["prefs"] = chrome_prefs
    chrome_prefs["profile.default_content_settings"] = {"images": 2}
    
    driver = webD.Chrome(options=chrome_options)
    return driver


def __init__(): 
    
    command = ""
    print("Hello PandaMan!\n")
    driver = startBrowser()
    
    while (command != "exit"):
        
        print("Give me the Panda Credentials!\n")
        email = input("PandaMail:")
        password = input("PandaPass:")
        driver, status = loginOnlyPanda(driver= driver, Passwors=password, Email=email)
        if(status == "Your Panda credentials are good!"):
            print (status)
            driver, fullName = getFullName(driver=driver)
            print("Your fullName is: "+ fullName.get_attribute("value")+"\n")
            command = input("Do you want ochange the name?(y/n)\n")
        else:
            print(status)
            status="login faild"
            command = "n"

        if(command.lower() == "y"):
            newName= input("New name:")
            dashboardChangeTheName(driver=driver, fullName=fullName, newName=newName, psw=password)
            driver, fullName = getFullName(driver=driver)
            print("Your new name is:" + fullName.get_attribute("value")+"\n")
            command = "n"
        else:
            command= input("Do you want ot reload the process?(y/n)\n")
        
        if(command.lower() == "n"):
            if(command.lower() == "n"):
                print("Have a nice day!")
                break
        
        if(command.lower() == "y"):
            if(status != "login faild"):
                driver = logOut(driver=driver)
                driver = startBrowser()
