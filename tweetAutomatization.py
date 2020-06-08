from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
#Sometimes doesn't work because twitter randomly change the homepage
driver.get('https://twitter.com')
#login
inputUsername = driver.find_element_by_name('session[username_or_email]')
inputUsername.send_keys('username')
inputPassword = driver.find_element_by_name('session[password]')
inputPassword.send_keys('password')
btnSubmitLogin = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/section/form/div/div[3]/div')
btnSubmitLogin.click()

#tweet
twInput=driver.find_element_by_class_name('public-DraftStyleDefault-block')
ActionChains(driver).move_to_element(twInput).click(twInput).send_keys("Asdasd").perform()
submitTweetBtn = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div[2]/div[3]')
submitTweetBtn.click()