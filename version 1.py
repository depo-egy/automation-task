from selenium import webdriver
from time import sleep


driver = webdriver.Chrome('D:/Programs/chromedriver')

driver.get('https://www.quora.com/login')
input('You need to log in in the browser window. Hit enter here when finished...')

url = input("enter the forum url")

driver.get(url)

answer_btn = driver.find_element_by_class_name('WriteAnswerPrimaryActionItem')
answer_btn.click()

sleep(8)
driver.execute_script("document.getElementsByClassName('content')[2].innerHTML = 'whatever'")

#sleep(10)
#b1 = driver.find_element_by_class_name('form_buttons')

#driver.find_element_by_xpath("//div[@class='form_buttons']//a[@class='submit_button']").click()

click = driver.find_elements_by_xpath("//a[@class='submit_button']")
click[2].click()

driver.quit()











'''
b1 = driver.find_element_by_xpath("//div[@class='form_buttons']//a[@class='submit_button']")
b1 = driver.find_element_by_xpath("//div[@class='form_buttons']//a[@id='__w2_w2UMvuvK25_inline_editor_submit']")
sleep(5)
b1.click()
'''
#comment = driver.find_element_by_class_name('content')

'''
comment = driver.find_element_by_id('__w2_wulkWv6N25_inline_editor_submit')

comment[3].click()
comment[3].send_keys('any comment')
comment[3].submit()

b1 = driver.find_element_by_id('__w2_wjNBfCO525_inline_editor_submit')
b1.click()

b1 = driver.find_element_by_class_name('form_buttons')
b2 = b1.find_element_by_class_name('inline_editor_buttons')
b3 =b2.find_element_by_class_name('submit_button')
b3.click()
'''
'''
comment = driver.find_element_by_class_name('doc')
c1 = comment.find_element_by_class_name('section')
c2= c1.find_element_by_class_name('span')
c3 = c2.find_element_by_class_name('content')
c3.text = 'dsds'
c5 = driver.find_element_by_class_name('inline_editor_buttons')
c6 = c5.find_element_by_class_name('submit_button')
c6.click()

comment = driver.find_element_by_class_name('doc')
c1 = comment.find_element_by_class_name('section')
c2= c1.find_element_by_class_name('span')
c3 = c2.find_element_by_class_name('content'
'''
