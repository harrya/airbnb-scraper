import requests
from bs4 import BeautifulSoup
import json
from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_page(url):
    options = Options()
    options.headless = True
    options.add_argument("--window-size=1920,1200")
    error = False
    try:  
        driver = webdriver.Firefox(options=options)
        driver.get(url)
        elem = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//div[@data-section-id='OVERVIEW_DEFAULT']/section/div/div/div/div/div/h2"))
        )

        output = {}
        overview = driver.find_element(By.XPATH, "//div[@data-section-id='OVERVIEW_DEFAULT']")

        title = overview.find_element(By.TAG_NAME, "h2").text
        output['title'] = title
        print(title)

        number_of_bedrooms = overview.find_elements(By.TAG_NAME, "span")[4].text
        output['number_of_bedrooms'] = number_of_bedrooms

        highlights = driver.find_element(By.XPATH, "//div[@data-section-id='HIGHLIGHTS_DEFAULT']")
        highlights_divs = highlights.find_elements(By.TAG_NAME, "div")

        property_type = highlights_divs[4].text
        property_type = property_type.replace('You’ll have the ', '')
        property_type = property_type.replace(' to yourself.', '')
        output['property_type'] = property_type
        return output
    except Exception as ex:
        print("scrape_page error")
        print(ex)
        error = True
    finally:
        driver.quit()
        
    if error:
        return "Page failed to load so could not scrape."

def main():
    try:
        urls = ["https://www.airbnb.co.uk/rooms/33571268",
                "https://www.airbnb.co.uk/rooms/20669368",
                "https://www.airbnb.co.uk/rooms/50633275"]
        outputs = []

        for url in urls:
            r = requests.get(url)
            print(r.status_code)
            if (r.status_code != 200):
                continue

            output = scrape_page(url)

            outputs.append(output)

        with open("output.txt", "w") as out:
            pprint(outputs, stream=out)
    except Exception as ex:
        print(ex)    
    
main()
