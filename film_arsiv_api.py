import requests


class theMovieDB:
    def __init__(self):
        self.api_url = "https://api.themoviedb.org/3"
        self.api_key = "<api_key>"


    def getPopulars(self):
        response = requests.get(f"{self.api_url}/movie/popular?api_key={self.api_key}&language=en-US&page=1")
        return response.json()

    def getSearchResult(self, keyword):
        response = requests.get(f"{self.api_url}/search/keyword?api_key={self.api_key}&query={keyword}&page=1")
        return response.json()



movieApi= theMovieDB()

while True:
    secim = input("1- popular movies\n2-search movies\n3- exit\nseçim: ")

    if  secim=="3":
        break
    else :
        if secim=="1":
            movies= movieApi.getPopulars()
            for movie in movies['results']:
                print(movie["title"])

        if secim=="2":
            keyword = input("keyword: ")
            movies.movieApi.getSearchResult(keyword)
            for movie in movies["results"]:
                print(movie["name"])
        



            








