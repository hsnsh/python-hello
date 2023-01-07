import requests


class TheMovieDb:
    def __init__(self):
        self.api_url = "https://api.themoviedb.org/3"
        self.api_key = "b68573786a3e56097b511d2db3e2cf96"

    def get_populars(self):
        response = requests.get(f"{self.api_url}/movie/popular?api_key={self.api_key}&language=en-US&page=1")
        return response.json()


movieCaller = TheMovieDb()
populars = movieCaller.get_populars()
for popular in populars['results']:
    print(popular['title'])
