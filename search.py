from selenium import webdriver

from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("http://python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.send_keys("pycon" + Keys.RETURN)
time.sleep(0.2)

assert "No results found" not in driver.page_source
driver.close()
