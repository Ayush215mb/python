from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

file=0
driver = webdriver.Chrome()
query= "laptop"
for i in range(1,4):
    driver.get(f"https://www.flipkart.com/search?q={query}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={i}")

    elems = driver.find_elements(By.CLASS_NAME, "tUxRFH")
    print(f"{len(elems)} items found" )
    for elem in elems:
       d= elem.get_attribute("outerHTML")
       with open(f"Flipkart/data/{query}_{file}.html", "w", encoding="utf-8") as f:
           f.write(d)
           file+=1

        


driver.close()
