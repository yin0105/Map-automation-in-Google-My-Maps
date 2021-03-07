
import datetime
import urllib.request  as urllib2 
from time      import sleep
from selenium  import webdriver
from multiprocessing import Pool
from itertools import product
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from fake_useragent import UserAgent
from datetime import datetime


processName = {}
def work_log(mail):
  url = 'https://accounts.google.com/'

#   browser_name = "Chrome"
  ua = UserAgent()
  userAgent = ua.random
  userAgent = userAgent.split(" ")
#   userAgent[0] = browser_name
  userAgent = " ".join(userAgent)
#   userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
  chrome_options = webdriver.ChromeOptions()
  chrome_options.add_argument('user-agent={0}'.format(userAgent))
  path = '.\\webdriver\\chromedriver.exe'
  chrome_options.add_argument('--log-level=0')
  driver = webdriver.Chrome (executable_path = path, options = chrome_options )

  try:
    driver.set_window_size(1024,900)
    processName[mail[0]] = logIn
    processName[mail[0]](mail, url, driver) #, proxies)
  except Exception as e:
    driver.save_screenshot(datetime.now().strftime("screenshot_%Y%m%d_%H%M%S_%f.png"))
    print(e)
    # driver.quit()
  finally:
    pass

      
def logIn(mail, url, driver): #, proxy_ip) :
  print("logging in...")
#   url_check = url.find("google")
  googleLogin(mail, driver)


def fail_with_error(message):
  def decorator(fx):
    def inner(*args, **kwargs):
      try:
        return fx(*args, **kwargs)
      except Exception as e:
        print(message)
        raise e
    return inner
  return decorator

@fail_with_error("Cannot set email address")
def google_set_login(driver, mail_address):
  try:
    email_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="identifierId"]')))
    email_field.send_keys(mail_address)
    print("Email address inserted")
  except TimeoutException:
    print("email field is not ready")
    pass

@fail_with_error("Cannot click login button")
def google_click_login_button(driver):
  try:
    login_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="identifierNext"]')))
    login_button.click()
    print("Login button clicked")
  except TimeoutException:
    print("login button is not ready")
    pass

@fail_with_error("Cannot set email password")
def google_set_password(driver, password):
  try:
    password_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')))
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')))
    password_field.send_keys(password)
    print("Password inserted")
  except TimeoutException:
    print("password field is not ready")
    pass

@fail_with_error("Cannot click next button")
def google_click_next_button(driver):
  try:
    next_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="passwordNext"]')))
    next_button.click()
    print("Next button clicked")
  except TimeoutException:
    print("next button is not ready")
    pass

# def google_is_security_question_required(driver):
#   try:
#     element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div/div')))
#     return element.text != "Request lacked state, may have been forged"
#   except:
#     pass
#   return True

# @fail_with_error("Cannot select security question as a login method")
# def google_select_security_question_as_login_method(driver):
#   try:
#     element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/ul/li[1]')))
#     element.click()
#     print("Log with security question")
#   except TimeoutException:
#     print("security question field is not ready")
#     pass

# @fail_with_error("Cannot set security answer")
# def google_set_security_ansver(driver, answer):
#   try:
#     security_question_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div/div[1]/div/div[1]/input')))
#     security_question_field.send_keys(answer)
#     print("Security question answer inserted")
#   except TimeoutException:
#     print("security question answer field is not ready")
#     pass

# @fail_with_error("Cannot confirm security answer")
# def google_confirm_security_question(driver):
#   try:
#     security_question_confirm_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button')))
#     security_question_confirm_button.click()
#     print("Security question confirm button clicked")
#   except TimeoutException:
#     print("security question confirm button is not ready")
#     pass

def googleLogin(mail, driver) :
  print("gmail logging in...")
  driver.get('https://accounts.google.com/signin/v2/identifier?passive=1209600&continue=https%3A%2F%2Fwww.google.com%2Fmaps%2Fd%2F&followup=https%3A%2F%2Fwww.google.com%2Fmaps%2Fd%2F&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
  mail_address = mail[1]
  mail_pass = mail[2]
  mail_active = mail[3]
  print("opend browser")
  google_set_login(driver, mail_address)
  google_click_login_button(driver)
  google_set_password(driver, mail_pass)
  google_click_next_button(driver)

#   if google_is_security_question_required(driver):
#     google_select_security_question_as_login_method(driver)
#     google_set_security_ansver(driver, mail_active)
#     google_confirm_security_question(driver)


work_log(["1", 'janwheeler197335@gmail.com', 'aleiivrc', 'nwxdrjem'])