import requests


class TheMovieDb:
    def __init__(self):
        self.api_url = "https://api.themoviedb.org/3"
        self.api_key = "b68573786a3e56097b511d2db3e2cf96"

    def get_populars(self):
        populars = requests.get(f"{self.api_url}/movie/popular?api_key={self.api_key}&language=en-US&page=1")
        return populars.json()

    def search_movie(self, s):
        results = requests.get(f"{self.api_url}/search/keyword?api_key={self.api_key}&language=en-US&page=1&query={s}")
        return results.json()


movieCaller = TheMovieDb()

while True:
    step = int(input("\n1- Get Popular Movies\n2- Search Movies\n9- EXIT\n\nSelect query type: "))
    if step == 9:
        print("Application terminated.")
        break
    else:
        if step == 1:
            response = movieCaller.get_populars()
            for popular in response['results']:
                print(popular['title'])
        elif step == 2:
            query = input("Query text: ")
            response = movieCaller.search_movie(query)
            for popular in response['results']:
                print(popular['name'])
        else:
            print("\nWrong operation select!")
            pass
