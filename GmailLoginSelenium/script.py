from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('http://gmail.com')
# driver.find_element("identifierId").send_keys('rajanmishra96034@gmail.com')
# driver.find_element('identifierNext').click()
# time.sleep(1)
# driver.find_element('password').send_keys('Rajanm@gmailpassword_1998')
# driver.find_element("passwordNext").click()

search_box = driver.find_element("Email or Phone")
search_box.send_keys("rajanmishra96034@gmail.com")
search_box.find_element("Next").click()