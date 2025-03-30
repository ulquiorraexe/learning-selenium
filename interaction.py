from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

result = driver.find_element(By.CSS_SELECTOR, value="div#articlecount a")
# print(result.text)
# all_portals = driver.find_element(By.LINK_TEXT, value="Content Portals")
# all_portals.click()
search = driver.find_element(By.NAME, value="search")
search.send_keys("Python", Keys.ENTER)
# driver.quit()