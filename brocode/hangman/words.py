
import requests
response = requests.get('https://www.wordgamedb.com/api/v1/words/random')
word = response.json()["word"]


