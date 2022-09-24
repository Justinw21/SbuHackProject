from selenium import webdriver
import pyautogui
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import os
import time

def searchAlli(x):
    options = webdriver.ChromeOptions()
    s = Service('C:\\WebDrivers\\chromedriver.exe')
    driver = webdriver.Chrome(service = s, options=options)
    driver.get("https://www.aliexpress.us/")
    driver.maximize_window()
    time.sleep(1)

    element = driver.find_element(By.CLASS_NAME, 'coupon-poplayer-modal')
    driver.execute_script("""
        var element = arguments[0];
        element.parentNode.removeChild(element);
        """, element)

    element1 = driver.find_element(By.CLASS_NAME, '_3KrBP')
    driver.execute_script("""
        var element = arguments[0];
        element.parentNode.removeChild(element);
        """, element1)
 
    time.sleep(1)

    search = driver.find_element(By.ID, "search-key")
    searchElement = ActionChains(driver).click(search).send_keys(x).send_keys(Keys.RETURN).perform()
    #time.sleep(2)
    #checkbox = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div[2]/div/div[1]/div[2]/div[1]/span[3]/span[4]/label/span[1]/input')
    #checkbox.click()

    time.sleep(2)

    findItem = True
    count = 0
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    results = soup.find_all('a', class_ ='_3t7zg _2f4Ho')
    print("Result Done!")
    item = results[0]

    url = "https:" + item.get('href')
    print(url)
    price = item.find('div', 'mGXnE _37W_B').text
    print(price)

    driver.get(url)
    try:
        rating=driver.find_element(By.CLASS_NAME, 'overview-rating-average').text
    except:
        rating=0

    print(rating)
    
    try:
        review_count=driver.find_element(By.XPATH, '//span[@class="product-reviewer-reviews black-link"]').text
    except:
        review_count=0

    print(review_count)
    arrival_date=driver.find_element(By.XPATH, "//div[@class='dynamic-shipping-line dynamic-shipping-contentLayout'][2]/span/span[2]").text
    print(arrival_date)
    

searchAlli("Texas Instruments TI-84 Plus Graphing Calculator Black With Cover")