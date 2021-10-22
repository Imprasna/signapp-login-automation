from selenium import webdriver #we need to install webdriver #pip install selenium
from getpass import getpass  #inbuild function
import pyautogui as pt 
import os
import platform


if platform.system() == 'Windows':
    print ("Yes");
    driver = webdriver.Chrome('C:\\\Program Files\\\chromedriver_win32\\\chromedriver.exe');

elif platform.system() == 'Windows':
    driver = webdriver.Chrome('C:\\\Program Files\\\chromedriver_win32\\\chromedriver.exe');
else:
    print ("It is not Windows Bro....:(")
    
print(os.name)
# print(platform.system())
print(platform.release())

# def login_automate():
#     username = 'prasanna.signatures1@gmail.com'
#     password = '123456'


#     driver = webdriver.Chrome()
#     driver.get('http://fibroinbeta.com/signapp_new')


#     username_textbox = driver.find_element_by_id('email')
#     username_textbox.send_keys(username)

#     password_textbox = driver.find_element_by_id('password')
#     password_textbox.send_keys(password)


#     login_button = driver.find_element_by_class_name('btn')
#     login_button.submit()



#     # if login_automate is True:
#     click_login = driver.find_element_by_id('timecard-clock-out')
#     click_login.click()
#     print('Hello')

#     position1 = pt.locateOnScreen("close.png", confidence = .8)
#     x = position1[0]
#     y = position1[1]
#     pt.moveTo(x + 165, y + 20, duration = .3)
#     pt.click()
#     close_dialog = driver.find_element_by_class_name('btn-default')

# login_automate()
