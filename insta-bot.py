# Привет , если поиск Python проекта еще актуален - напиши плз в телегу @freshaccs,  либо по мылу freshaccs () yahoo.com

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import random


email = "<your_email_here>"
password = "<your_password_here>"

browser = webdriver.Firefox()
browser.implicitly_wait(5)

browser.get('https://www.instagram.com/accounts/login/')

emailInput = browser.find_elements_by_css_selector('form input')[0]
passwordInput = browser.find_elements_by_css_selector('form input')[1]

emailInput.send_keys(email)
passwordInput.send_keys(password)
passwordInput.send_keys(Keys.ENTER)
time.sleep(2)

notnow = browser.find_element_by_css_selector('html.js.logged-in.client-root.js-focus-visible.sDN5V body div#react-root section._9eogI.E3X2T main.SCxLW.o64aR div.Igw0E.rBNOH.YBx95._4EzTm div.pV7Qt.DPiy6.Igw0E.IwRSH.eGOV_._4EzTm.qhGB0.ZUqME div.Igw0E.IwRSH.eGOV_._4EzTm.MGdpg.aGBdT div.cmbtv button.sqdOP.yWX7d.y3zKF')
notnow.click()

hashtag_list = ['trip', 'traveler']

tag = -1
likes = 0

for hashtag in hashtag_list:
    tag += 1
    browser.get('https://www.instagram.com/explore/tags/'+ hashtag_list[tag] + '/')

    photo = browser.find_element_by_css_selector('#react-root > section > main > article > div.EZdmt > div > div > div:nth-child(1) > div:nth-child(1) > a')
    ref = photo.get_property('href')

    browser.get(ref)

    like = browser.find_element_by_css_selector('.fr66n > button:nth-child(1)')
    like.click()

    likes += 1
    time.sleep(random.randint(18, 25))

browser.close()
