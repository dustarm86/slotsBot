import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('https://discordapp.com/channels/209843539109085184/471722679448240128')
assert '#slots_addicts' in browser.title

# selects ps4 as console and clicks on it via xpath
text_field = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/form/div/div/textarea")
text_field.send_keys('t!slots')
time.sleep(10)