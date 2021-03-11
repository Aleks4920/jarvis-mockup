import requests


url = ('https://newsapi.org/v2/top-headlines?'
       'country=ca&'
       'apiKey=0380784c8ac94149b85ae2e1dc336c49')
response = requests.get(url).json()
def latest():
    y = ''
    for x in range(3):
        try:
            y += '.' + (response['articles'][x]['title'])

        except:
            break
    return str(y)
