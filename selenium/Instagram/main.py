from selenium import webdriver
from selenium.webdriver.common.by import By
import time

file=0
driver = webdriver.Chrome()
username= "ayush215mb"

# xl565be x1m39q7l x1uw6ca5 x2pgyrj
driver.get("https://www.facebook.com/facebook/photos")

elems = driver.find_elements(By.CLASS_NAME, "xzg4506" )

# print(f"{len(elems)} items found" )
for elem in elems:
    d= elem.get_attribute("innerHTML")
    with open(f"Instagram/data/facebook_{file}.html", "w", encoding="utf-8") as f:
        f.write(d)
        file+=1

        


driver.close()
