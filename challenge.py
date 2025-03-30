from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

first = driver.find_element(By.NAME, value="fName")
last = driver.find_element(By.NAME, value="lName")
mail = driver.find_element(By.NAME, value="email")

first.send_keys("Yasmin", Keys.TAB)
last.send_keys("Serdengeçti", Keys.TAB)
mail.send_keys("minniethepuf@gmail.com", Keys.ENTER)