import requests

def fact():
    url = "https://api.chucknorris.io/jokes/random"

    response = requests.request("GET", url)

    return str(response.json()['value'])
