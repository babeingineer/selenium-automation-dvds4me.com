import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


df = pd.read_excel('DVDs4me 022024.xlsx', dtype={1: str})

id_column = df.iloc[:, 1]
quantity_column = df.iloc[:, 8]


driver = webdriver.Chrome()
for i in range(len(id_column)):
    print(id_column[i])
    try:
        response = requests.get('https://dvds4me.com/search?q=' + id_column[i])
        soup = BeautifulSoup(response.text, 'html.parser')
        element = soup.select_one('.full-unstyled-link')
        if element:
            url = element.get('href')
            print(url)

            
            driver.get('https://dvds4me.com' + url)
            quantity_input = driver.find_element(By.CLASS_NAME, 'quantity__input')
            quantity_input.send_keys(Keys.DELETE)  # product-form__submit
            quantity_input.send_keys(int(quantity_column[i]))

            submit_btn = driver.find_element(By.CLASS_NAME, 'product-form__submit')
            submit_btn.click()
        else:
            print("nothing")
    except Exception as e:
        print("Error occued")

time.sleep(100000)
driver.quit()