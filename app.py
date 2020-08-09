from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import re

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://web.whatsapp.com")

input("Press anything after QR scan")
time.sleep(8)

names = ["Bui Airtel","Rahul Tgt","Gaurav Tgt Whatsapp"]

while True:
    for name in names:
        time.sleep(2)
        person = driver.find_element_by_xpath('//span[@title="{}"]'.format(name))
        time.sleep(2)
        person.click()

        for i in range(1,3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        msg_got = driver.find_elements_by_css_selector("span._3Whw5.selectable-text.invisible-space.copyable-text")
        msg = [message.text for message in msg_got]

        if re.search(".*@deepak|hello|hey|Hello|Hey|@Deepak|Deepak|deepak.*", msg[-1]):
            reply = driver.find_elements_by_class_name("_3FRCZ.copyable-text.selectable-text")[1]
            reply.clear()
            reply.send_keys("Yes.. I'm offline, my chatbot is listening!")
            reply.send_keys(Keys.RETURN)