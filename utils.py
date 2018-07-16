from selenium import webdriver
import re
from ebay_entry import *


def get_product_collection(driver):
    pe_list = []    #list of product_entries
    products = driver.find_elements_by_class_name("s-item")

    i = 0
    for p in products:
        try:
            index = i
            item_name = p.find_element_by_class_name("s-item__title").text
            item_subtitle = p.find_element_by_class_name("s-item__subtitle").text
            link = p.find_element_by_class_name("s-item__link").get_attribute('href')
            print (item_name)
            print (item_subtitle)
            print (link)
            details = p.find_elements_by_class_name("s-item__details")
            for d in details:
                raw_str = d.get_attribute('innerHTML')

                if (re.search("s-item__price", raw_str)):
                    print(re.match(".*s-item__price.*\$(\d+.\d+)", raw_str)).group(0)
                #begin parse of raw string




            return
        except Exception as e:
            raise e

        # pe = product_entry(
        #         index=0,
        #         item_name=p.find_element_by_class_name("s-item__title").text,
        #         item_subtitle=p.find_element_by_class_name("s-item__subtitle").text,
        #         link = p.find_element_by_class_name('s-item__link').text,
        # )

        # print(p.find_element_by_class_name("s-item__link").text)
        # details = p.find_elements_by_class_name("s-item__details")

        # for d in details:
        #    str = d.get_attribute('innerHTML')
        # print raw html of details
        # re.compile("<div.*s-item__price\">(?P<price>\d+\.\d+).*)