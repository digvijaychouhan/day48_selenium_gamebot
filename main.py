from selenium import webdriver

chrome_driver_path = "C:/Development/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.python.org/")

event_times = driver.find_elements_by_css_selector(".event-widget .shrubbery .menu time")
event_names = driver.find_elements_by_css_selector(".event-widget .shrubbery .menu a")
events = {n: {"time": event_times[n].text, "name": event_names[n].text} for n in range(len(event_times))}

# for n in range(len(event_names)):
#     events[n] = {
#         "time": event_times[n].text,
#         "name": event_names[n].text
#     }


print(events)



# ele1 = driver.find_element_by_id("id-search-field")
# print(ele1.get_attribute("name"))

# ele2 = driver.find_element_by_name("q")
# print(ele2.get_attribute("placeholder"))

# logo = driver.find_element_by_class_name("python-logo")
# print(logo.get_attribute("src"))

# documentation_link = driver.find_element_by_css_selector(".documentation-widget a")
# print(documentation_link.text)

# bug_link = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

# driver.close()
driver.quit()
