from selenium import webdriver #we need to install webdriver #pip install selenium
from getpass import getpass  #inbuild function
import pyautogui as pt 
import os
import platform
from datetime import datetime, timedelta
from threading import Timer
# import Scheduler
# from apscheduler.schedulers.blocking import BlockingScheduler





def login_automate():
    username = 'prasanna.signatures1@gmail.com'
    password = '123456'

    username_textbox = driver.find_element_by_id('email')
    username_textbox.send_keys(username)

    password_textbox = driver.find_element_by_id('password')
    password_textbox.send_keys(password)

    login_button = driver.find_element_by_class_name('btn')
    login_button.submit()

    # if login_automate is True:
    click_login = driver.find_element_by_id('timecard-clock-out')
    click_login.click()
    print('Hello')

if platform.system() == 'Windows': 
    
    print (platform.system());
    print(datetime.today());

    x=datetime.today()
    y=x.replace(day=x.day+0, hour=15, minute=31, second=0, microsecond=0)

    delta_t=y-x
    secs=delta_t.seconds+1
    print (y)

    t = Timer(secs, login_automate)
    t.start()


    driver = webdriver.Chrome('C:\\\Program Files\\\chromedriver_win32\\\chromedriver.exe');
    driver.get('http://fibroinbeta.com/signapp_new')

elif platform.system() == 'Linux': 
    print (platform.system());
    driver = webdriver.Chrome();
    driver.get('http://fibroinbeta.com/signapp_new')
    # driver = webdriver.Chrome()

else:
    print ("Unsupported browser bro....:(")

    # username_textbox = driver.find_element_by_id('email')
    # username_textbox.send_keys(username)

    # password_textbox = driver.find_element_by_id('password')
    # password_textbox.send_keys(password)


    # login_button = driver.find_element_by_class_name('btn')
    # login_button.submit()



    # # if login_automate is True:
    # click_login = driver.find_element_by_id('timecard-clock-out')
    # click_login.click()
    # print('Hello')

    position1 = pt.locateOnScreen("close.png", confidence = .8)
    x = position1[0]
    y = position1[1]
    pt.moveTo(x + 165, y + 20, duration = .3)
    pt.click()
    close_dialog = driver.find_element_by_class_name('btn-default')

login_automate()

# if platform.system() == 'Windows': 
    
#     print (platform.system());
#     driver = webdriver.Chrome('C:\\\Program Files\\\chromedriver_win32\\\chromedriver.exe');

# elif platform.system() == 'Linux': 
#     print (platform.system());
#     driver = webdriver.Chrome();


    # login_automate()

# else:
#     print ("It is not Windows neither linux Bro....:(")
    
# print(os.name)
# print(platform.system())
# print(platform.release())

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
