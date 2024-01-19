from bs4 import BeautifulSoup
import requests
import re
import time
import csv
from selenium import webdriver
import ftfy

base_link = "https://www.wildberries.ru/catalog/"

base_link = "https://www.wildberries.ru/catalog/151346319/detail.aspx"
driver = webdriver.Firefox()


def get_price(soup: BeautifulSoup):  
    price_str = (soup
            .div
            .main
            .find('div', class_='main__container')
            .div
            .find('div', style='display: block;')
            .div
            .find('div', class_='product-page__grid')
            .find('div', class_='product-page__aside')
            .div
            .div
            .find('div', class_='product-page__price-block product-page__price-block--aside')
            .div
            .div
            .div
            .p
            .span
            .ins
            .contents
        )[0]
    
    return ftfy.fix_text(price_str).strip()
    
    
    
driver = webdriver.Firefox()
with open('wildberries.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    for idx in range(10 ** 6, 2 * 10 ** 6):
        new_link = f'{base_link}/{idx}/detail.aspx'
        driver.get(new_link)
        time.sleep(2)
        page = driver.execute_script('return document.body.innerHTML')
        soup = BeautifulSoup(''.join(page), 'html.parser')
        
        price = get_price(soup)
        print(price)
        
        break
        
        # print(soup)