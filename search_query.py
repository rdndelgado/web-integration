from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get('https://www.google.com/')
time.sleep(5)
search_box = driver.find_element(By.NAME, 'q')  # 'q' is the name attribute for the search input field

search_query = 'Search here'

for i in search_query:
    search_box.send_keys(i)
    time.sleep(0.25)

result = search_box.send_keys(Keys.RETURN)  #storing the result to a variable

time.sleep(5)

#next
#retrieve the data of the result
    