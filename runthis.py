from selenium import webdriver #we need to install webdriver #pip install selenium
from getpass import getpass  #inbuild function

def login_automate():
    username = 'prasanna.signatures1@gmail.com'
    password = '123456'

    driver = webdriver.Chrome()
    driver.get('http://fibroinbeta.com/signapp_new')


    username_textbox = driver.find_element_by_id('email')
    username_textbox.send_keys(username)

    password_textbox = driver.find_element_by_id('password')
    password_textbox.send_keys(password)


    login_button = driver.find_element_by_class_name('btn')
    login_button.submit()