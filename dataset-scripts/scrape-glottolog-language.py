import requests
# pip3 install beautifulsoup4
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time
import csv

# brew install postgresql
# pip install psycopg2-binary
import psycopg2
import eilcommon

options = Options()
options.headless = True

file = open('data-glottolog-org-language.csv', 'w+', newline='')

# Download chromedriver and set the PATH environment variable or hardcode the executable_path in webdriver.Chrome function
# For more details about setting up chrome driver, see this documentation. https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--disable-gpu")
driver = webdriver.Chrome(
    executable_path='/home/aslam/programs/chromedriver_linux64/chromedriver', chrome_options=chrome_options)


URL = "https://glottolog.org/glottolog/language"
driver.get(URL)

time.sleep(3)
soup = BeautifulSoup(driver.page_source, 'lxml')

dataTable = soup.find(id="Families")
page = 1
thead = dataTable.find_all("thead")
tbody = dataTable.find_all("tbody")
titleCols = thead[0].find_all("tr")[0].find_all('th')
titles = [ele.text.strip() for ele in titleCols]
nextPage = True
with file:
    writer = csv.writer(file)
    writer.writerow(titles)
    dataRows = tbody[0].find_all("tr")

    for dataRow in dataRows:
        dataCols = dataRow.find_all('td')
        dataCols = [ele.text.strip() for ele in dataCols]
        writer.writerow(dataCols)

    print("Page " + str(page) + ":Data Fetched")
    page = page + 1
    elm1 = driver.find_element_by_css_selector("#Families_paginate ul li.next")

    while nextPage == True:

        # currentPage = driver.find_element_by_xpath('//*[@id="Families_paginate"]/ul/li[@class="active"]/a')
        elm1 = driver.find_element_by_css_selector(
            "#Families_paginate")
        nextA = driver.find_element_by_css_selector("li.next a")
        nextLi = driver.find_element_by_css_selector("li.next")

        if not 'disabled' in nextLi.get_attribute('class').split():
            nextA.click()
            time.sleep(3)

            soup = BeautifulSoup(driver.page_source, 'lxml')
            dataTable = soup.find(id="Families")
            thead = dataTable.find_all("thead")
            tbody = dataTable.find_all("tbody")
            titleCols = thead[0].find_all("tr")[0].find_all('th')
            titles = [ele.text.strip() for ele in titleCols]
            dataRows = tbody[0].find_all("tr")
            for dataRow in dataRows:
                dataCols = dataRow.find_all('td')
                dataCols = [ele.text.strip() for ele in dataCols]
                writer.writerow(dataCols)

            print("Page " + str(page) + ":Data Fetched")
            page = page + 1
        else:
            print("End")
            nextPage = False
            break

driver.close()
