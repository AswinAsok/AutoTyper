import pyautogui
import time
from selenium import webdriver



browser = webdriver.Chrome(executable_path='C:/Users/Aswin Asok/chromedriver/chromedriver.exe')
time.sleep(10)
browser.get(input("Enter The URL : "))

time.sleep(15)

totalwords = len((browser.find_element_by_xpath("//*[@id='row1']")).find_elements_by_tag_name("span"))

i = 1

while i < totalwords:
    if i == 1:
        starttime = time.time()
        print(starttime)

    word=browser.find_element_by_class_name("highlight").get_attribute("innerHTML")
    pyautogui.typewrite(word)
    currenttime = time.time()
    pyautogui.press("space")

    if currenttime - starttime > 60:
        print(currenttime - starttime)
        break

    i=i+1


