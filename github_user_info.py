# from selenium import webdriver
# import time


# class Github:
#     def __init__(self,username, passwrord):
#         self.browser = webdriver.Edge()
#         self.username = username
#         self.passwrord = passwrord
#         self.follwers= []

#     def signIn (self ):
#         self.browser.get("https://github.com/login")
#         time.sleep(2)


#         self.browser.find_element_by_xpath("//*[@id='login_field']").send_keys(self.username)
#         self.browser.find_element_by_xpath("//*[@id='password']").send_keys(self.passwrord)

#         time.sleep(1)

#         self.browser.find_element_by_xpath("//*[@id='login']/div[4]/form/input[14]").click()

#     def getFollowers(self):
#         self.browser.get(f"https://github.com/{self.username}?tab=followers")
#         time.sleep(2)

#         items = self.browser.find_element_by_css_selector(".d-table.table-fixrd")

#         for i in items:
#             self.follwers.append(find_element_by_css_selector(".link-gray.p1-1").text)

# git= Github(username, passwrord)

# git.signIn()
# git.getFollowers()
# print(git.follwers)




from selenium import webdriver
import time

class Github:
    def __init__(self, username, password):
        self.browser = webdriver.Firefox()
        self.username = username
        self.password = password
        self.followers = []

    def signIn(self):
        self.browser.get("https://github.com/login")
        time.sleep(2)

        self.browser.find_element_by_xpath("//*[@id='login_field']").send_keys(self.username)
        self.browser.find_element_by_xpath("//*[@id='password']").send_keys(self.password)

        time.sleep(1)

        self.browser.find_element_by_xpath("/html/body/div[3]/main/div/div[4]/form/input[14]").click()

    def loadFollowers(self):
        items = self.browser.find_elements_by_css_selector(".d-table.table-fixed")

        for i in items:
            self.followers.append(i.find_element_by_css_selector(".link-gray.pl-1").text)


    def getFollowers(self):
        self.browser.get(f"https://github.com/{self.username}?tab=followers")
        time.sleep(2)

        self.loadFollowers()

        while True:
            links = self.browser.find_element_by_class_name("BtnGroup").find_elements_by_tag_name("a")

            if len(links) == 1:
                if links[0].text == "Next":
                    links[0].click()
                    time.sleep(1)
                    self.loadFollowers()

                else:
                    break
            else:
                for link in links:
                    if link.text == "Next":
                        link.click()
                        time.sleep(1)
                        self.loadFollowers()
                    else:
                        continue

username = input("username giriniz: ")
password = input("password giriniz: ")
github = Github(username, password)
github.signIn()
github.getFollowers()
print(len(github.followers))
print(github.followers)




























