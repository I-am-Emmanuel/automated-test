from selenium import webdriver

chrome_web = webdriver.Chrome()

chrome_web.get('https://www.seleniumeasy.com/')

# assert 'Selenium' in chrome_web.title
# button_text = chrome_web.find_element_by_class_name('btn-button')
button_text2 = chrome_web.find_element_by_css_selector('#get-input > .btn')

# button_text.get_attribute('innerHTML')
# print( button_text)
# assert 'Message box' in chrome_web.page_source

input_text = chrome_web.find_element_by_id('user-message')

input_text.clear()
input_text.send_keys('I AM EXTRA COOOOL')

button_text.click()

output_message = chrome_web.get_element_by_id('display')
assert 'I AM EXTRA COOOOL' in output_message.text


# chrome_web.quit()

# chrome_web.close()
# chrome_web.close()
