import time
from logging import exception

from selenium import webdriver as webD
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys




def loginOnlyPanda(driver : webD, Passwors: str, Email: str):
    base_url = "https://app.pandascore.co/login"

    driver.get(base_url)

    
    links = driver.find_elements(By.XPATH,"//*[@href]")
    button = driver.find_element(By.TAG_NAME,"input")
    
    email = driver.find_element(By.NAME,"email")
    password = driver.find_element(By.NAME,"password")
    
    email.send_keys(Email)
    password.send_keys(Passwors)

    button.submit()

    driver.execute_script("arguments[0].click();",button)
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
        #print("Your full name is: " + fullName.get_attribute("value")+"\n")
    except Exception:
        print("Something'g rong!")
    
    return driver , fullName;


def dashboardChangeTheName(driver: webD, fullName: any, newName: str, password: str):
    
    driver = driver

    button = driver.find_element(By.CLASS_NAME,"btn-panda")
    
    password = driver.find_element(By.XPATH,"//span[contains(text(),'Current password')]/following-sibling::*[1]")
    password.send_keys(password)

    fullName.send_keys(Keys.BACKSPACE)
    for i in str(fullName):
        fullName.send_keys(Keys.BACKSPACE)
    
    fullName.send_keys(newName)
    try:
        button.submit()
    except Exception:
        print("Something'g rong!")
    
    time.sleep(5)
    

def __init__():
    driver = webD.Chrome(ChromeDriverManager().install())
    time.sleep(5)
    command = ""
    print("Hello PandaMan!\n")
    case = 0
    
    while (command != "exit"):
        
        print("Give me the Panda Credentials!\n")
        email = input("PandaMail:")
        password = input("PandaPass:")
        driver, status = loginOnlyPanda(driver= driver, Passwors=password, Email=email)
        if(status == "Your Panda credentials are good!"):
            print (status)
            driver, fullName = getFullName(driver=driver)
            print("Your fullName is: "+ fullName.get_attribute("value")+"\n")
            command = input("Doyou want to change your name?(y/n)")
            if(command == "y"):
                newName= input("New name:")
                dashboardChangeTheName(driver=driver, fullName=fullName, newName=newName, password=password)
                driver, fullName = getFullName(driver=driver)
                print("Your new name is:" + fullName.get_attribute("value")+"\n")
            if(command == "n"):
                print("Have a nice day!")
                break
        else:
            print (status+"\n")
            command= input("Do you want ot reload the process?(y/n)\n")
            if(command == "n"):
                print("Have a nice day!")
                break
        command = input("Do you want ot reload  the process?(y/n)\n")
        if(command == "n"):
            print("Have a nice day!")
            break

__init__()
