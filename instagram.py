from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import bs4, platform,getpass
from os import system, name 
def requestpassword():          
                driver = driver = webdriver.Firefox(executable_path=r'C:\Users\user\Downloads\geckodriver-v0.28.0-win64\geckodriver.exe')
                driver_name = input("Enter the name you want :") 
                driver_get =("https://www.instagram.com/accounts/password/reset/?source=auth_switcher")
                driver.get(driver_get)
                time.sleep(3)
                username = driver.find_element_by_name('cppEmailOrUsername')
                username.send_keys(driver_name)
                submit = driver.find_element_by_tag_name('form')
                submit.submit()
                driver.find_element_by_class_name("_7UhW9   xLCgt      MMzan   _0PwGv         uL8Hv         ").text
                print("Wanna close the browser")

def loginoninstagram():
                driver_username = input("Username : ")
                driver_password = input("Password : ")
                driver_instagram =("https://www.instagram.com/accounts/login/?source=auth_switcher")
                driver = driver = webdriver.Firefox(executable_path=r'C:\Users\user\Downloads\geckodriver-v0.28.0-win64\geckodriver.exe')
                driver_get = (driver_instagram)
                user=driver.find_element_by_name("username")
                user.send_keys(driver_username)
                time.sleep(1)
                psswd = driver.find_element_by_name("password")
                passwd.send_keys(driver_password)
                sumbitbmit = driver.find_element_by_tag_name('form')
                submit.submit()


##def registeroninstagram

def userjson(Instagram_name = None):
                import urllib.request,json
                with urllib.request.urlopen("https:https://www.instagram.com/",instagram_name + "/?__a=1"):
                                data = json.loads(url.read().decode())
                                
                
                
def WelcomeStuffs():
                import sys, webbrowser
                print("Operation-System", platform.platform(),platform.release(),platform.version())
                print("User-Name:", getpass.getuser())
                get_ip_and_name()
                print("Wanna continue ? Type Y/N")
                user_input = input("What you wish to do: ")
                if (user_input == "Y"):
                                clear_screen = system('cls')
                                print("What do you prefer to do")
                                print("Type 1 to restore your password")
                                print("Type 2 To login on your instagram account")
                                user_input2 = input("Enter a command: ")
                                if (user_input2 == 1):
                                                requestpassword()
                                elif (user_input2 == 2):
                                                loginoninstagram():
                                elif 
                elif (user_input == "N"):
                                sys.exit()
                else:
                                print("Something went wrong. if you have any issue contact me on instagram! #ogcoockie# ")
                                webbrowser.open('instagram.com/ogcoockie')
                                time.sleep(3)
                                sys.exit()




                             
def get_ip_and_name():
                import socket,urrlib.request,json
                hostname = socket.gethostname()
                IPAddr = socket.gethostbyname(hostname)
                print("Your computer name is : ", hostname)
                print("Your ip addresses is :", IPAddr)
                               
                                

                
WelcomeStuffs()
