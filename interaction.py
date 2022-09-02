from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:/Development/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("http://secure-retreat-92358.herokuapp.com/")

fname = driver.find_element_by_name("fName")
fname.send_keys("Divijay")

lname = driver.find_element_by_name("lName")
lname.send_keys("Chouhan")

email = driver.find_element_by_name("email")
email.send_keys("digvijay@outlook.in")

btn = driver.find_element_by_class_name("btn")
btn.click()

# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# action = driver.find_element_by_id("searchButton")
# search = driver.find_element_by_name("search")
# search.send_keys("Python")
# action.click()
# search.send_keys(Keys.ENTER)

# wiki_stats = driver.find_element_by_css_selector("#articlecount a")
# print(wiki_stats.text)
# driver.quit()
