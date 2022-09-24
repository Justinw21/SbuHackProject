from ssl import ALERT_DESCRIPTION_BAD_CERTIFICATE_HASH_VALUE
from selenium import webdriver
import pyautogui
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import os
import time

def searchAmazon(x):
    options = webdriver.ChromeOptions()
    s = Service('C:\\WebDrivers\\chromedriver.exe')
    driver = webdriver.Chrome(service = s, options=options)
    driver.get("https://www.amazon.com/")
    driver.maximize_window()
    element = driver.find_element(By.ID, "twotabsearchtextbox")
    searchElement = ActionChains(driver).click(element).send_keys(x).send_keys(Keys.RETURN).perform()

    fitler=driver.find_element(By.CLASS_NAME, "a-dropdown-container")
    print("Working")
    fitlerClick=ActionChains(driver).move_to_element(fitler).click(fitler).perform()
    time.sleep(1)
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('enter')
    time.sleep(1)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    results = soup.find_all('div', {'data-component-type': 's-search-result'})
    item = results[0]
    atag = item.h2.a
    url = "https://amazon.com" + atag.get('href')
    print(url)
    parent_price = item.find('span', 'a-price')
    price = parent_price.find('span', 'a-offscreen').text
    print(price)
    rating = item.i.text
    print(rating)
    review_count = item.find('span', {'class':'a-size-base s-underline-text'}).text
    print(review_count)
    arrival_date = item.find('span', {'class':'a-color-base a-text-bold'}).text
    print(arrival_date)

    return url, price, rating, review_count, arrival_date
