from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import html
import csv
import pandas as pd
import requests

# specify the path to the webdriver

driver = webdriver.Chrome()

# driver.get(url='https://www.linkedin.com/posts/chawlamanish_nocode-edtech-elearning-activity-6993464111695052801-wQOM?utm_source=share&utm_medium=member_desktop')
driver.get(url='https://www.linkedin.com/feed/update/urn:li:activity:7026746732856098816/')

src = driver.page_source #itwosrked
# page = requests.get(str("https://www.linkedin.com/feed/update/urn:li:activity:6993464111695052801/"))

soup = BeautifulSoup(src,"html.parser") #itworked

# # locate the element containing the number of likes
# like_element = driver.find_element(By.CLASS_NAME, "social-details-social-counts__social-proof-fallback-number")
# print(like_element.text)

# intro = soup.find('span', class_='font-normal ml-0.5') #itworked
intro = soup.find('span', class_='ca-entry-point__num-views t-14') #itworked
print(intro) #itworked


# extract the number of likes
# likes = int(like_element.text)

# print the number of likes
# print(f'Number of likes: {likes}')

# close the browser
# driver.quit()


