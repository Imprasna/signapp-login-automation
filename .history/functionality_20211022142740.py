from selenium import webdriver #we need to install webdriver #pip install selenium
from getpass import getpass  #inbuild function
import pyautogui as pt 
import os
import platform


if platform.system() == 'Windows':
    print (platform.system());
    driver = webdriver.Chrome('C:\\\Program Files\\\chromedriver_win32\\\chromedriver.exe');
    login_automate()

elif platform.system() == 'Linux':
    print (platform.system());
    driver = webdriver.Chrome();
    login_automate()

else:
    print ("It is not Windows neither linux Bro....:(")
    
# print(os.name)
# print(platform.system())
# print(platform.release())


