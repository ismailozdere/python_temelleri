from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver =webdriver.Edge()

url = "http://github.com"
driver.get(url)


searchInput= driver.find_element_by_name("q")
time.sleep(1)
searchInput.send_keys("python")
time.sleep(2)
searchInput.send_keys(keys.ENTER)
time.sleep(2)

# result = driver.page_source
# print(result)

# result = driver.find_element_by_css_selector(".repo-list-item h3 a")

# for element in result:
#     print(element.text)





driver.close()















