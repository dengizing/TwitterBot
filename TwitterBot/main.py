from twitterUserInfo import username,password
from selenium import webdriver
from selenium.webdriver.common.keys import  Keys
import time

class Twitter:
    def __init__(self, username, password):
        self.browserProfile =webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs',{'intl.accept_languages'})#tarayıcımız ingilizce açmak istediğimden tarayıcımın kabul edip aktifettirdiğim diller
        self.browser =webdriver.Chrome('chromedriver.exe',chrome_options=self.browserProfile)#
        self.username =username
        self.password=password

    def singIn(self):
        self.browser.get("https://twitter.com/login")
        time.sleep(2)

        usernameInput =self.browser.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/fieldset/div[1]/input")
        passwordInput =self.browser.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/fieldset/div[2]/input")

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)

        btnSubmit =self.browser.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form//div[2]/button")
        btnSubmit.click()

        time.sleep(2)

    def search(self,hashtag):
        searchInput =self.browser.find_element_by_xpath("//")
        searchInput.send_keys(hashtag)
        time.sleep(2)
        searchInput.send_keys(Keys.ENTER)
        time.sleep(2)

        loopCounter = 0
        last_height = self.browser.execute_script("return document.documentElement.scrollHeight")
        while True:
            if loopCounter > 3:
                break

            self.browser.execute_script(
                "window.scrollTo(0,document.documentElement.scrollHeight);")  # scroll çalıştığında en sondaki konuma kadar gidiyoruz.
            time.sleep(2)
            new_height = self.browser.execute_script("return document.documentElement")
            if last_height == new_height:  # son çektiğimiz scroll uzunluğu yeni tüm scroll a eşitse orada dursun
                break
            last_height = new_height
            loopCounter += 1


        list=self.browser.find_element_by_xpath("//")
        for item in list:
            print(len(list))
            print("*********")
            print(item.text)
'''

sürekli yüklenen ve kaybolan tweetler bir liste içine koyalım ve tüm tweetleri alma ve dosyaya kaydetme'''

'''
ben browserda aradığım şeyi incele dediğimde ve consola girdiğimde 
scroll un taradığı uzunluk ve diğer seçenekleri baktığımda

document.documentElement.scrollHeight-->Bu benim scroll daki uzunluğumu  belirtir.
burda java script kodunu alıyorum.



'''


twitter =Twitter(username,password)
#login
twitter.singIn()
twitter.search("python")