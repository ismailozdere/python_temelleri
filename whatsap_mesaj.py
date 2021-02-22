from selenium import webdriver
class whatsap:
    def __init__(self , yazı):
        self.browser = webdriver.firefox
        self.yazılacak =yazı
        



    def yazılacak (self):
        self.browser.get("https://web.whatsapp.com")
        self.browser.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/div/div/div[15]").click()
        
        while True:
            yazılacak= self.browser.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]")


yazı=input("söyle: ")
söyle= whatsap(yazı)
söyle.yazılacak


