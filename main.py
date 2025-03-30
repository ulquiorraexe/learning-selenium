from selenium import webdriver
from selenium.webdriver.common.by import  By

#Keep the browser open after program finishes
# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=options)
# driver.get("https://www.amazon.com/Logitech-Wireless-Headset-Black-Tico/dp/B081415GCS/ref=sr_1_13?_encoding=UTF8&sr=8-13")
#
# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole").text
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction").text
# print(f"The price is {price_dollar}.{price_cents}")
#
# driver.quit()

#driver.close() -- closes the tab
#driver.quit() -- closes the browser

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("https://python.org")
event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text
    }
print(events)
driver.quit()