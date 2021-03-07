from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from fake_useragent import UserAgent
# from pynput.keyboard import Listener as key_listener
# import time
# import pprint
# import msvcrt
# import time, threading


####################### Main #################################
print("1")
ua = UserAgent()
print("16")
userAgent = ua.random
print("17")
userAgent = userAgent.split(" ")
# userAgent[0] = "Chrome"
userAgent = " ".join(userAgent)
print(userAgent)
# userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('user-agent={0}'.format(userAgent))


activateListener = False
path = '.\\webdriver\\chromedriver.exe'
chrome_options.add_argument('--log-level=0')
browser = webdriver.Chrome (executable_path = path, options = chrome_options )
browser.get("https://www.google.com/maps/d/")
elem = browser.find_element_by_xpath("//input[@type='email']")
elem.clear()
elem.send_keys("evgenyashyvaevaweb@gmail.com")
elem = browser.find_element_by_xpath("//button/span[text()='Next']/parent::button")
elem.click()

# elem = browser.find_element_by_xpath("//span[text()='+ Create a new map']/parent::span/parent::div")
# elem.click()

# //div[@data-tooltip="Import data from a CSV file, spreadsheet or KML."]

# for elem in elems:
#     pprint.pprint(elem)

# # elem.send_keys(webdriver.common.keys.Keys.RETURN)

# elem = browser.find_element_by_partial_link_text("Log In") 
# elem.click()

# ########################  Log In  ###################################
# try:
#     elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@class='NativeElement ng-untouched ng-pristine ng-invalid ng-star-inserted' and @type='email']")))
# except:
#     print("Log In timed out.")
# elem.clear()
# elem.send_keys("evgenyashyvaevaweb@gmail.com")
# elem = browser.find_element_by_xpath("//input[@class='NativeElement ng-untouched ng-pristine ng-invalid ng-star-inserted' and @type='password']")
# elem.clear()
# elem.send_keys("Shamora_bich_2020")
# elem = browser.find_element_by_xpath("//button[@class='ButtonElement ng-star-inserted' and @type='submit']")
# elem.click()

# time.sleep(5)
# browser.get("https://www.freelancer.com/search/projects") 

# time.sleep(5)
# activateListener = True
# original_window = browser.current_window_handle

