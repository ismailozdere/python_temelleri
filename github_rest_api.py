import requests



class Github:
    def __init__(self):
        self.api_url = "https://api.github.com"
        self.token = '<token_bilgisi>'


    def getUser(self, username):
        response = requests.get(self.api_url+"/users/"+username)
        return response.json()

    def getRepositories(self, username):
        response= requests.get(self.api_url+"/users/"+username+"/repos")
        return response.json() 

    def createRepository(self, name):
        requests.post(self.api_url+"/user/repos?access_token="+self.token, json={
            "name": name,
            "description": "This is your first repository",
            "homepage": "https://sadikturan.com",
            "private": False,
            "has_issues": True,
            "has_projects": True,
            "has_wiki": True
        })

git=Github()

while True:
    secim =input("1- find user\n2- get repository\n3- create repository\n4- exit\nseçim: ")
    if secim=="4":
        break
    else:
        if secim=="1":
            username = input("username: ")
            result= git.getUser(username)
            print(f"name: {result['name']} public repos: {result['public_repos']} follower : {result['followers']} ")
        if secim=="2":
            username= input("username: ")
            result = git.getRepositories(username)
            for repo in result:
                print(repo["name"])

        if secim=="3":
            name = input("repository name: ")
            result = git.createRepository(name)
            print(result)

        else:
            print("yanlış bir seçim")



























