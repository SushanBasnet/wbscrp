from selenium import webdriver
import re
from ebay_entry import *
from utils import *
import os

if (os.name == 'nt'):
    driver = webdriver.Chrome(os.path.join(os.getcwd(), 'chromedriver.exe'))
else:
    driver = webdriver.Chrome()

driver.get("http://www.ebay.com")

search_item = "Imax B6AC charger"

# get text-area
textarea = driver.find_element_by_id("gh-ac")
#clear and write search item
textarea.clear
textarea.send_keys(search_item)
#click search
search_button = driver.find_element_by_id("gh-btn")
search_button.click()

num_results = driver.find_element_by_class_name("srp-controls__count-heading")
#results
print(num_results.text)
num_results = re.split(" ", num_results.text)[0]
if int(num_results) is 0:
    print("result is zero, no data to analyze")
    quit()

#we have a non-zero result..gather top 50 product data
pr_list = get_product_collection(driver)
#driver.close()



#gather item of top 50 relevant product and prep 50 ebay_entries
#dump JSON of product data
#analyze and represent data



